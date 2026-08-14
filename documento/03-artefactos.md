# 3. Artefactos

Un artefacto es una pieza concreta del ciclo: algo que se define, se aprueba y queda registrado. Son seis. Tres organizan el trabajo y tres son el producto de la construcción.

## Los que organizan el trabajo

| Artefacto | Qué es |
|---|---|
| **Intent** | Lo que se quiere lograr, dicho en términos de negocio. El equipo define el destino y la IA propone el camino. |
| **Unit** | Una parte del sistema que se construye y se entrega por sí sola. Un Intent se descompone en Units; equivalen a los subdominios del diseño guiado por el dominio o a las épicas de Scrum. |
| **Bolt** | El ciclo en que se construye un Unit. Es lo que en Scrum era el sprint, pero de horas o días en lugar de semanas. Un Unit puede necesitar varios Bolts. |

## Los que produce la construcción

| Artefacto | Qué es |
|---|---|
| **Domain Design** | La lógica de negocio de un Unit, sin decidir todavía la tecnología. La IA modela con diseño guiado por el dominio: agregados, entidades, objetos de valor, eventos, repositorios. |
| **Logical Design** | El mismo diseño, ya resuelto para los requisitos no funcionales y con los patrones de arquitectura que correspondan. Cada decisión queda registrada en un ADR que una persona valida. |
| **Deployment Units** | El paquete listo para desplegar: el código ejecutable, su configuración y su infraestructura. |

Un requisito no funcional describe qué tan bien hace el sistema lo que hace: cuánto tarda, cuánto aguanta, qué registra, qué protege.

Ninguno de los seis se descarta al cerrar la fase. Todos quedan guardados y la IA los usa como memoria de contexto durante el resto del ciclo: el diseño recuerda lo que se decidió en los requisitos, y el despliegue recuerda lo que se decidió en el diseño.
