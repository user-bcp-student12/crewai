"""Agente inicial del taller. Mejora sus instrucciones sin cambiar su contrato."""
from crewai import Agent, Task
from crew.llm_config import llm

KEY = 'testing'
LABEL = 'Ingeniero de pruebas'
SPEC_FILE = 'testing_report.md'
EXTRACT_CODE = True

INSTRUCTIONS = "Realiza la tarea de tu rol."
agent = Agent(role='Ingeniero de pruebas que verifica criterios de aceptación, contratos de API y persistencia',
              goal="Entregar testing_report.md, pruebas y comandos reproducibles: relacionar cada criterio de "
                   "aceptación con una prueba y su resultado esperado, incluir casos positivos, negativos, de "
                   "borde e integración, detallar preparación, datos de prueba, comandos y limpieza, y comprobar "
                   "los contratos de API y persistencia y las correcciones propuestas.",
              backstory="Eres un ingeniero de pruebas riguroso y basado en evidencia. Nunca inventas resultados: "
                        "cuando no tienes una salida real, marcas la prueba como NO EJECUTADO.", llm=llm,
              verbose=True, allow_delegation=False)


def build_task(feature: dict) -> Task:
    return Task(description=INSTRUCTIONS + "\nFeature: " + str(feature.get("title", ""))
                + "\n" + str(feature.get("description", ""))
                + "\n" + str(feature.get("acceptance_criteria", [])),
                expected_output=('testing_report.md con cada criterio de aceptación relacionado con una prueba y su resultado '
                                 'esperado; casos positivos, negativos, de borde e integración; preparación, datos de '
                                 'prueba, comandos reproducibles y limpieza; verificación de los contratos de API y '
                                 'persistencia y de las correcciones propuestas; y las pruebas ejecutables. Las pruebas '
                                 'sin salida real se marcan NO EJECUTADO, sin inventar resultados.'), agent=agent)
