# Tabla de contenidos — Metodología AI-DLC de Grupo TX

Documento corto, espina = el método de AWS. Las tres secciones centrales (3, 4 y 5) son las mismas tres partes en que el paper organiza el método, y en el mismo orden que la presentación del 12 de agosto. Lo construido para el harness entra solo como complemento en la sección 6; sus etapas no estructuran nada.

## 1. El método

Qué es AI-DLC y de dónde viene: paper de Raja SP (julio 2025), re:Invent (diciembre 2025), repositorio abierto, adaptación a servicios financieros (mayo 2026). El mental model en una frase: la IA propone planes y pregunta; el equipo decide. Ni autocompletar código, ni dejar que la IA construya sola. Qué hace este documento: cómo lo aplica el área.

*Fuentes: slides 1–3 de la presentación; blog de lanzamiento; Method Definition Paper.*

## 2. Alcance: cuándo aplica y cuándo no

Qué trabajo recorre el ciclo completo y qué trabajo no lo necesita; el propio método excluye los sistemas simples. La regla operativa por cambio: ¿hace falta spec? — cuatro criterios; en duda, no. Quién decide en los casos dudosos.

*Pendiente del acuerdo del equipo (criterios y ejemplos del área). La regla por cambio se rescata del flujo del harness.*

## 3. Artefactos

Los seis, en dos familias. Los que organizan el trabajo: Intent, Unit, Bolt. Los que produce la construcción: Domain Design, Logical Design, Deployment Units. Un Unit es una parte del sistema; un Bolt, un ciclo de horas o días.

*Fuente: slide 5; paper.*

## 4. Fases y rituales

Inception (Mob Elaboration: la IA propone historias, criterios y Units; el equipo corrige lo sobre- y lo sub-diseñado). Construction (Mob Construction y Mob Testing; el Product Owner vuelve para las pruebas). Operations (despliegue, monitoreo, incidentes; AWS no definió ritual — aquí va lo nuestro). Dentro de cada fase, sus puntos de validación: qué no avanza sin el Aprobado de una persona.

*Fuente: slide 6; blog de lanzamiento.*

## 5. El flujo

Los nueve pasos del paper, del intent al despliegue. El recorrido según el punto de partida: sistema nuevo, o sistema existente con la etapa de elevar el código a modelos (estático y dinámico) — casi todo lo que mantenemos ya existe.

*Fuente: slides 7–8; paper.*

## 6. Cómo lo practicamos: herramientas y skills

El complemento del método: qué atiende cada fase, en una tabla fase → herramienta/skill → estado [Real]/[Propuesto]. Las skills rescatadas del diseño del harness (onboarding, exploración, ejecución, tdd, api, testing, recibir-revisión, revisión) mapeadas a la fase que sirven. El enforcement mínimo que sobrevive: guard de git y CI. La metodología apunta, no duplica: cada herramienta documenta la suya.

*Se rescata del harness: las skills, el guard, el CI. Se descarta: sus cinco etapas como estructura, el panel fijo de seis agentes y la mecánica de rondas — sobre-ingeniería para el estado actual del equipo.*

## 7. Gobernanza

La regla de oro (§13.5, política vigente): todo código generado por IA pasa revisión humana; el merge lo ejecuta siempre una persona identificable; ningún agente es Accountable de nada. Trazabilidad de la historia al código y a la prueba; qué evidencia queda y qué puede reconstruir un auditor.

*Fuente: política de gobernanza de IA; blog de servicios financieros (mayo 2026) para el lenguaje de entornos regulados.*

## 8. Adopción

El primer día: qué se lee, qué se instala, cuál es el primer trabajo acompañado. La vara la fija el paper: el método se practica en un día, sin capacitación formal; esta sección se mide contra eso.

## Anexos

- **A. Glosario** — AI-DLC, Intent, Unit, Bolt, Mob Elaboration, spec, PASS/DENY/DENYSPEC; convenciones (qué queda en inglés).
- **B. Plantillas** — requirements.md, design.md, tasks.md.
- **C. Un cambio recorriendo el ciclo completo** — ejemplo ilustrativo de punta a punta.
- **D. Correspondencia con AI-DLC Workflows 2.0** — las 5 fases y 33 etapas de la implementación GA mapeadas contra las 3 fases de este documento, para que el documento no se reescriba cuando AWS reorganice.

## Documento hermano

Informe del caso piloto: el primer trabajo real medido con el método. Hereda la medición completa — línea base estimada por escrito antes de empezar, indicadores que se vigilan entre sí, nunca métricas por persona — y se publica y versiona aparte.

---

### Decisiones que esta tabla ya incorpora

1. Fuera el contexto institucional y la sección de Medición (rojo del borrador): lo primero es material comercial; lo segundo vive en el documento hermano.
2. El documento no abre con Alcance: abre con una página de método (sección 1).
3. La espina es AWS v1 (3 fases, como la presentación); la v2 queda en el anexo D como mapa.
4. Del harness propio se conservan las skills y las reglas simples; sus etapas no estructuran el documento.
5. Siguen pendientes del equipo: criterios de Alcance (sección 2) y si se agregan Principios propios — si se aprueban, entran como bloque corto dentro de la sección 1, no como sección aparte.
