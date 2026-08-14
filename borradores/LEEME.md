# Borradores

Los dos documentos de trabajo que existen hoy, en orden de madurez:

## `2026-08-12_metodologia-aidlc-grupotx-v0.2.0.pdf` (+ transcripción editable en `metodologia-v0.2.0.md`)

La metodología **ya escrita**, versión 0.2.0. Documento único interno, 13 páginas: fases con práctica propia (spec → Bolts → revisión por agentes con veredicto PASS/DENY/DENYSPEC → merge humano), las cuatro capas (Estándar/Skill/Agente/Enforcement), inventario de herramientas con marcadores [Real]/[Propuesto], mapa de trazabilidad contra AWS v1 y v2, glosario y checklist de madurez (M1–M6, veredicto EN CONSTRUCCIÓN). Nació el 12 ago como reescritura de un kit de 33 documentos que se descartó.

## `2026-08-13_tabla-de-contenidos-borrador.docx`

Índice comentado previo ("Borrador para discusión"): solo el Contexto desarrollado; el resto son secciones con contenido previsto. Trae resaltados del 12 ago:

- **Rojo** (se elimina): contexto institucional (§I.1) y Medición (§VI).
- **Amarillo** (pendiente de decisión del equipo): Alcance (§I.2) y Principios (§II).
- **Verde**: Gobernanza (fragmento) y el "Documento hermano" (informe del caso piloto, que hereda la medición).

## Relación entre los dos

El PDF v0.2.0 ya resuelve por diseño la mayor parte de lo que el índice de Word dejaba abierto: el rojo no existe en él, el Alcance se volvió la decisión "¿hace falta spec?" por cambio (§4.1), la Medición son las medidas de §8 con la regla de no reportar lo no instrumentado, y la estructura es la del documento corto interno. Lo que el Word planificaba y el PDF aún no tiene: Principios comentados, Adopción/primer día, plantillas de los artefactos y el ejemplo de un cambio recorriendo el ciclo completo.
