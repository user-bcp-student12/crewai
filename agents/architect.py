"""Agente inicial del taller. Mejora sus instrucciones sin cambiar su contrato."""
from crewai import Agent, Task
from crew.llm_config import llm

KEY = 'architect'
LABEL = 'Arquitecto'
SPEC_FILE = 'user_story.md'
EXTRACT_CODE = False

INSTRUCTIONS = "Realiza la tarea de tu rol."
agent = Agent(role='Arquitecto de datos y persistencia (modelo relacional y migraciones SQL)',
              goal="Partiendo de la arquitectura aprobada y del esquema existente, enumerar entidades, "
                   "atributos, tipos y cardinalidades; definir claves primarias y foráneas, nulabilidad, "
                   "unicidad, índices y reglas de integridad; proponer migraciones compatibles con los datos "
                   "existentes con su orden y comprobaciones previas y posteriores; incluir pruebas de "
                   "relaciones, duplicados y valores inválidos y un plan de reversión o recuperación; "
                   "coordinar el contrato de persistencia con Backend; y entregar data_spec.md con "
                   "propuestas SQL sin ejecutar migraciones ni borrar datos.",
              backstory="Eres un arquitecto con experiencia en modelado relacional, integridad referencial "
                        "y migraciones seguras sobre datos existentes. Nunca ejecutas migraciones ni borras "
                        "datos: solo propones SQL revisable, con verificaciones de integridad y recuperación. "
                        "Acuerdas con Backend el contrato de persistencia para que ambos trabajen sobre el "
                        "mismo esquema.", llm=llm,
              verbose=True, allow_delegation=False)


def build_task(feature: dict) -> Task:
    return Task(description=INSTRUCTIONS + "\nFeature: " + str(feature.get("title", ""))
                + "\n" + str(feature.get("description", ""))
                + "\n" + str(feature.get("acceptance_criteria", [])),
                expected_output='Una historia de usuario.', agent=agent)
