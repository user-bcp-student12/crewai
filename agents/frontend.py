"""Agente inicial del taller. Mejora sus instrucciones sin cambiar su contrato."""
from crewai import Agent, Task
from crew.llm_config import llm

KEY = 'frontend'
LABEL = 'Desarrollador frontend'
SPEC_FILE = 'frontend_spec.md'
EXTRACT_CODE = True

INSTRUCTIONS = "Realiza la tarea de tu rol."
agent = Agent(role='Desarrollador frontend Angular que implementa el recorrido del usuario según el contrato de API aprobado',
              goal="Implementar el recorrido del usuario según el contrato de API aprobado: definir campos, validaciones, "
                   "acciones y mensajes; cubrir estados de carga, vacío, éxito y error; evitar envíos duplicados; "
                   "conservar etiquetas accesibles, navegación por teclado y foco visible; e incluir cómo comprobar "
                   "el recorrido y sus errores. Entregar frontend_spec.md y código Angular con el formato de extracción "
                   "que exige build_task.",
              backstory="Eres un desarrollador frontend Angular con experiencia en formularios, validaciones y consumo de APIs. "
                        "Parte siempre del contrato de API aprobado y no inventas endpoints ni campos. Cuidas los estados de "
                        "carga, vacío, éxito y error, bloqueas los envíos duplicados y garantizas accesibilidad: etiquetas "
                        "accesibles, navegación por teclado y foco visible. Documentas cómo comprobar el recorrido y sus errores.", llm=llm,
              verbose=True, allow_delegation=False)


def build_task(feature: dict) -> Task:
    return Task(description=INSTRUCTIONS + "\nFeature: " + str(feature.get("title", ""))
                + "\n" + str(feature.get("description", ""))
                + "\n" + str(feature.get("acceptance_criteria", [])),
                expected_output='frontend_spec.md con el recorrido del usuario según el contrato de API aprobado: campos, '
                                'validaciones, acciones y mensajes; estados de carga, vacío, éxito y error; prevención de envíos '
                                'duplicados; accesibilidad (etiquetas accesibles, navegación por teclado, foco visible); y cómo '
                                'comprobar el recorrido y sus errores. Además, código Angular en bloques markdown; primera línea '
                                'de cada bloque con // nombre.service.ts (o el nombre del archivo correspondiente).', agent=agent)
