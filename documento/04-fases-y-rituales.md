# 4. Fases y rituales

Cómo se ordena el trabajo a lo largo del ciclo y cómo trabaja el equipo en cada fase.

[Figura 3 — El ciclo completo]

## Inception: qué construir y por qué

La IA propone las historias de usuario, los criterios de aceptación, los requisitos no funcionales, los riesgos y la descomposición del Intent en Units. El equipo revisa esa propuesta en vivo y corrige lo que está sobre-diseñado o lo que quedó corto. Ese ritual es la Mob Elaboration, y en él participan el Product Owner, los desarrolladores y la IA. La fase cierra con los Units aprobados y los Bolts sugeridos para construirlos.

## Construction: cómo construirlo

Cada Unit se construye en uno o más Bolts. La IA modela el dominio, resuelve los requisitos no funcionales y genera el código con sus pruebas. Los equipos intercambian las especificaciones de integración y deciden los patrones de arquitectura: es la Mob Construction. Para validar el resultado contra lo que se pidió, el Product Owner vuelve a la mesa en la Mob Testing. La fase cierra con Deployment Units probados.

## Operations: mantenerlo vivo

Despliegue, observabilidad e incidentes, con la IA analizando métricas, registros y trazas para anticipar anomalías. No tiene un ritual propio. Es la fase que el paper describe con menos detalle, y la que la implementación 2.0 de AWS desarrolló después en siete etapas, desde la tubería de despliegue hasta la respuesta a incidentes.

## Los puntos de validación

Ninguna fase avanza sola. En cada paso la IA presenta su propuesta y espera; el trabajo continúa cuando una persona la aprueba.
