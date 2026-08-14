# 5. El flujo

El ciclo se recorre en nueve pasos, del Intent al sistema en producción.

[Figura 2 — El flujo: nueve pasos, tres fases]

El recorrido empieza con un plan. La IA lee la intención de negocio y propone los pasos necesarios para llevarla a cabo; el equipo lo revisa, lo corrige y lo aprueba. Después la IA descompone cada paso en tareas más finas, bajo la misma revisión. Cada paso deja artefactos que el siguiente usa como contexto, y por eso el orden importa.

## Sistema nuevo y sistema existente

Los nueve pasos son los mismos en los dos casos. La diferencia está al principio de Construction: cuando el sistema ya existe, antes de modelar el dominio hay que elevar el código a un modelo.

La IA lee el código y produce dos representaciones. El modelo estático muestra los componentes del dominio, sus responsabilidades y sus relaciones. El modelo dinámico muestra cómo esos componentes interactúan para resolver los casos de uso principales. Los desarrolladores y el Product Owner revisan y corrigen ambos modelos antes de continuar; con eso resuelto, el resto del recorrido es igual al de un sistema nuevo.
