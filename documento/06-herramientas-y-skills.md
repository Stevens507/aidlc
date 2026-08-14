# 6. Herramientas y skills

Cada fase se apoya en herramientas concretas. El inventario indica cuáles están en uso y cuáles son propuesta.

Una skill es un paquete de estándares e instrucciones que la herramienta carga sola cuando la tarea coincide. Sirve para que todos sigan el mismo proceso sin tener que recordarlo.

| Fase | Herramientas y skills | Estado |
|---|---|---|
| Inception | Kiro para las specs: requirements, design y tasks | Propuesto |
| Construction | Claude Code con las reglas del repositorio y las skills de dominio; Forge para la revisión, con veredicto PASS, DENY o DENYSPEC | Real |
| Operations | El CI de cada proyecto, con definiciones por stack | Real |

Las reglas viven en cada repositorio y los agentes las cargan como contexto: estilo de Python, patrones de Terraform, convenciones de pruebas. Las skills del área hoy están dispersas entre repositorios; unificarlas en una familia común es trabajo pendiente.

Una regla que importa no se queda escrita. Baja al CI o a un hook de git, donde actúa sin que nadie se acuerde de invocarla.

La metodología apunta, no duplica: cada herramienta mantiene su propia documentación.
