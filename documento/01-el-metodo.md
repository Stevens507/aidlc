# 1. El método

AI-DLC es la metodología que AWS publicó para construir software con IA generativa. Raja SP definió el método en un white paper en julio de 2025. AWS lo presentó en re:Invent en diciembre de ese año, liberó la implementación como código abierto (awslabs/aidlc-workflows, licencia MIT-0) y en mayo de 2026 publicó una adaptación para servicios financieros.

La idea central cabe en una frase: la IA propone, el equipo decide. En cada actividad del desarrollo, la IA analiza el contexto y presenta un plan. Cuando le falta información, pregunta. El equipo corrige lo que haga falta y aprueba; recién entonces la IA implementa. El mismo ciclo se repite en los requisitos, en el diseño, en el código, en las pruebas y en el despliegue.

[Figura 1 — La IA propone, el equipo decide]

AWS parte de un diagnóstico: las dos formas habituales de usar IA en desarrollo quedaron cortas. El asistente que autocompleta hace tareas sueltas, sin contexto del sistema. La IA autónoma que construye sola entrega software que nadie del equipo entiende ni puede defender ante un cliente. AI-DLC toma otro camino: pone a la IA en el centro del proceso y a una persona en cada decisión.

Este documento describe cómo el equipo de IA Generativa de Grupo TX aplica el método. Conserva las fases y el vocabulario de AWS; donde el material de AWS no dice nada, pone práctica propia y la marca como tal. Está escrito para que quien entra al equipo lo lea completo y entienda cómo se trabaja sin que nadie se lo explique.
