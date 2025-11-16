from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.message import Message
import asyncio

class SymptomCollectorAgent(Agent):
    class SendMsgBehaviour(OneShotBehaviour):
        async def run(self):
            msg = Message(to="diagnosis_agent@desktop-fhat8kf")  # recipient
            msg.body = "Hello from Symptom Collector"
            await self.send(msg)
            print("Message sent!")

    async def setup(self):
        print("Symptom Collector starting...")
        self.add_behaviour(self.SendMsgBehaviour())

class DiagnosisAgent(Agent):
    class ReceiveMsgBehaviour(OneShotBehaviour):
        async def run(self):
            msg = await self.receive(timeout=10)  # wait for 10 sec
            if msg:
                print(f"Received: {msg.body}")
            else:
                print("No message received.")

    async def setup(self):
        print("Diagnosis Agent starting...")
        self.add_behaviour(self.ReceiveMsgBehaviour())

async def main():
    sc_agent = SymptomCollectorAgent("symptomcollector@desktop-fhat8kf", "sm123")
    da_agent = DiagnosisAgent("diagnosis_agent@desktop-fhat8kf", "d123")

    await sc_agent.start()
    await da_agent.start()

    await asyncio.sleep(15)  # wait for messages
    await sc_agent.stop()
    await da_agent.stop()

asyncio.run(main())
