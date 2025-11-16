import asyncio
from agents.symptom_collector import SymptomCollectorAgent
from agents.diagnosis_agent import DiagnosisAgent
from agents.treatment_agent import TreatmentAgent
from agents.supervisor_agent import SupervisorAgent
from config.settings import *

async def main():
    a1 = SymptomCollectorAgent(SYMPTOM_COLLECTOR_JID, SYMPTOM_COLLECTOR_PASS)
    a2 = DiagnosisAgent(DIAGNOSIS_JID, DIAGNOSIS_PASS)
    a3 = TreatmentAgent(TREATMENT_JID, TREATMENT_PASS)
    a4 = SupervisorAgent(SUPERVISOR_JID, SUPERVISOR_PASS)

    await a1.start()
    await a2.start()
    await a3.start()
    await a4.start()

    print("All agents running...")

    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
