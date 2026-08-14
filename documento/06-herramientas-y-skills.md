# 6. Herramientas y skills

El método no depende de una plataforma. Define qué capacidad hace falta en cada fase; cada proyecto la cubre con la herramienta que tenga.

| Fase | Qué capacidad hace falta | Con qué se cubre hoy | Estado |
|---|---|---|---|
| Inception | Producir la spec en tres artefactos, cada uno con aprobación explícita | Kiro | Propuesto |
| Construction | Un asistente que cargue las reglas del repositorio, y una revisión con veredicto antes de integrar | Claude Code; Forge | Real |
| Operations | Verificaciones automáticas en cada cambio | El CI de cada proyecto, con definiciones por stack | Real |

Una skill es un paquete de estándares e instrucciones que la herramienta carga sola cuando la tarea coincide. Sirve para que todos sigan el mismo proceso sin tener que recordarlo. Las reglas funcionan igual: viven en cada repositorio y los agentes las cargan como contexto — estilo de Python, patrones de Terraform, convenciones de pruebas.

Una regla que importa no se queda escrita. Baja al CI o a un hook de git, donde actúa sin que nadie se acuerde de invocarla.

La metodología apunta, no duplica: cada herramienta mantiene su propia documentación.
