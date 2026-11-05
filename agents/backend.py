"""Agente inicial del taller. Mejora sus instrucciones sin cambiar su contrato."""
from crewai import Agent, Task
from crew.llm_config import llm

KEY = 'backend'
LABEL = 'Desarrollador backend'
SPEC_FILE = 'backend_spec.md'
EXTRACT_CODE = True

INSTRUCTIONS = "Realiza la tarea de tu backend."
agent = Agent(role='Desarrollador backend Java (endpoints, servicios y acceso a datos)',
              goal="Implementar los endpoints y servicios del plan respetando el contrato de API, "
                   "validando entradas y devolviendo errores coherentes; definir acceso a datos y "
                   "transacciones (en equipos de seis, también esquema y migraciones; con Datos, "
                   "consumir su contrato sin duplicar sus migraciones); y entregar backend_spec.md "
                   "con un caso válido, un error y los comandos para comprobarlos, más el código Java.",
              backstory="Eres un desarrollador backend Java senior con experiencia en APIs REST, "
                        "validación de entradas, manejo uniforme de errores, persistencia y "
                        "transacciones. Sigues el contrato de API del plan sin alterarlo, y cuando "
                        "existe un agente de Datos usas su contrato en lugar de duplicar sus "
                        "migraciones. Documentas cómo verificar tu trabajo con casos y comandos "
                        "reproducibles.", llm=llm,
              verbose=True, allow_delegation=False)


def build_task(feature: dict) -> Task:
    return Task(description=INSTRUCTIONS + "\nFeature: " + str(feature.get("title", ""))
                + "\n" + str(feature.get("description", ""))
                + "\n" + str(feature.get("acceptance_criteria", [])),
                expected_output="Dos entregables. (1) backend_spec.md: endpoints y servicios implementados según el "
                                "contrato de API, reglas de validación y formato de errores coherente, acceso a "
                                "datos y transacciones (en equipos de seis, esquema y migraciones; con Datos, "
                                "referencia a su contrato sin duplicar migraciones), un caso válido, un caso de "
                                "error y los comandos para comprobarlos. (2) Código Java en bloques markdown; "
                                "primera línea de cada bloque con // Nombre.java y package pe.bcp.login.service.",
                agent=agent)

