"""Agente inicial del taller. Mejora sus instrucciones sin cambiar su contrato."""
from crewai import Agent, Task
from crew.llm_config import llm

KEY = 'security'
LABEL = 'Revisor de seguridad'
SPEC_FILE = 'security_report.md'
EXTRACT_CODE = False

INSTRUCTIONS = "Revisa autenticación, autorización, entradas, secretos, datos sensibles e inyección; entrega hallazgos, correcciones y comprobaciones."
agent = Agent(role='Analista de seguridad de aplicaciones',
              goal="Identificar riesgos de autenticación, autorización, entradas, secretos, datos sensibles e inyección, y proponer correcciones verificables.",
              backstory="Eres un analista de seguridad metódico. Sustentas cada hallazgo con evidencia del código y evitas afirmaciones no comprobadas.",
              llm=llm,
              verbose=True, allow_delegation=False)


def build_task(feature: dict) -> Task:
    return Task(description=INSTRUCTIONS + "\nFeature: " + str(feature.get("title", ""))
                + "\n" + str(feature.get("description", ""))
                + "\n" + str(feature.get("acceptance_criteria", [])),
                expected_output='Un informe con hallazgos de seguridad, evidencia y ubicación, nivel de severidad, correcciones recomendadas y comprobaciones realizadas.', agent=agent)
