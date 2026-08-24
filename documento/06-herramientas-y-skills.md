# 6. HERRAMIENTAS Y SKILLS

El método no depende de una plataforma. Define qué capacidad hace falta en cada fase; cada proyecto la cubre con la herramienta que tenga.

<!-- anchos: 1575,3105,3465,1395 -->
| **Fase** | **Qué capacidad hace falta** | **Con qué se cubre hoy** | **Estado** |
|---|---|---|---|
| Inception | Producir la spec en tres artefactos, cada uno con aprobación explícita | Kiro | Real |
| Construction | Un asistente que cargue las reglas del repositorio, y una revisión con veredicto antes de integrar | Claude Code; Forge, orquestación de corridas autónomas con revisores y veredicto PASS/DENY/DENYSPEC | Real |
| Operations | Verificaciones automáticas en cada cambio | El CI de cada proyecto, con definiciones por stack | Real |

La herramienta importa menos que lo que se le carga. Una skill es un paquete de estándares e instrucciones que la herramienta levanta sola cuando la tarea coincide, y con eso todos recorren el mismo camino sin tener que acordarse de nada.

**Cada herramienta mantiene su propia documentación. Pero documentar una regla no es suficiente:** si de verdad importa, debe salir de la documentación y bajar al CI o a un hook de Git, donde pueda hacerse cumplir automáticamente.
