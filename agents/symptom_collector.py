from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from config.settings import *
from .llm import extract_symptoms_with_llm
import openai

class SymptomCollectorAgent(Agent):
    class CollectBehaviour(CyclicBehaviour):
        async def run(self):
            user_input = input("Please describe your symptoms: ")

            # Use LLM to extract symptoms
            extracted_symptoms = extract_symptoms_with_llm(user_input)

            if not extracted_symptoms:
                print("[SymptomCollector] Could not detect symptoms. Please try again.")
                return

            # Send extracted symptoms to Diagnosis Agent
            msg = Message(
                to=DIAGNOSIS_JID,
                body=",".join(extracted_symptoms),
                metadata={"performative": "request", "type": "symptoms"}
            )
            await self.send(msg)
            print("[SymptomCollector] Sent symptoms to Diagnosis Agent:", extracted_symptoms)

            # Wait for final output from Supervisor
            final_msg = await self.receive(timeout=30)
            if final_msg:
                print("[SymptomCollector] Final Output:", final_msg.body)
                await self.agent.stop()

    async def setup(self):
        print("[SymptomCollector] Agent started")
        self.add_behaviour(self.CollectBehaviour())

