"""Agente inicial del taller. Mejora sus instrucciones sin cambiar su contrato."""
from crewai import Agent, Task
from crew.llm_config import llm

KEY = 'chapter'
LABEL = 'Chapter'
SPEC_FILE = 'chapter_review.md'
EXTRACT_CODE = False

INSTRUCTIONS = "Realiza la tarea de tu rol."
agent = Agent(role='Chapter', goal="Completar la tarea asignada.",
              backstory="Eres un integrante del equipo.", llm=llm,
              verbose=True, allow_delegation=False)


def build_task(feature: dict) -> Task:
    description = (INSTRUCTIONS + "\nFeature: " + str(feature.get("title", ""))
                   + "\n" + str(feature.get("description", ""))
                   + "\n" + str(feature.get("acceptance_criteria", [])))
    return Task(
        description=description,
        expected_output="Un informe de revisión final con veredicto APROBADO, "
        "APROBADO CON CONDICIONES o RECHAZADO, hallazgos sustentados en evidencia "
        "y acciones pendientes verificables.",
        agent=agent,
    )
