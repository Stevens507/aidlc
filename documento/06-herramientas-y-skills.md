# 6. Herramientas y skills

El método no depende de una plataforma. Define qué capacidad hace falta en cada fase; cada proyecto la cubre con la herramienta que tenga.

| Fase | Qué capacidad hace falta | Con qué se cubre hoy | Estado |
|---|---|---|---|
| Inception | Producir la spec en tres artefactos, cada uno con aprobación explícita | Kiro | Propuesto |
| Construction | Un asistente que cargue las reglas del repositorio, y una revisión con veredicto antes de integrar | Claude Code; Forge, orquestación de corridas autónomas con revisores y veredicto PASS/DENY/DENYSPEC | Real |
| Operations | Verificaciones automáticas en cada cambio | El CI de cada proyecto, con definiciones por stack | Real |

La herramienta importa menos que lo que se le carga. Una skill es un paquete de estándares e instrucciones que la herramienta levanta sola cuando la tarea coincide, y con eso todos recorren el mismo camino sin tener que acordarse de nada.

Ese mecanismo tiene un límite: funciona mientras alguien lo invoque. Por eso una regla que importa de verdad no se queda escrita, baja al CI o a un hook de git y actúa sin que nadie la llame.

El resto se queda donde ya está. La metodología apunta y no duplica: cada herramienta mantiene su propia documentación.
