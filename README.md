# Metodología AI-DLC — Grupo TX

Repositorio de trabajo para redactar el documento de metodología del área: cómo el equipo de IA Generativa aplica AI-DLC (AI-Driven Development Life Cycle), el método que AWS publicó en julio de 2025. El objetivo es un documento corto y legible: quien entra al equipo debería poder leerlo y entender el procedimiento completo sin que nadie se lo explique.

## Qué hay aquí

```
fuentes/                  Todo el material oficial de AWS, descargado el 14 ago 2026
├── FUENTES.md            Índice comentado: qué es cada fuente, fecha y URL original
├── paper/                Method Definition Paper (Raja SP, jul 2025) — PDF + texto extraído
├── especificacion/       Especificación AI-DLC Workflows 2.0 — PDF + texto extraído
├── blogs/                Los 4 blogs oficiales en inglés, más un espejo local de sus imágenes
├── blogs-regionales/     9 casos publicados en blogs oficiales de AWS Japón, Corea y China
├── terceros/             4 lecturas externas: dos consultoras y dos corridas reales de la 2.0
└── repo-oficial/         Snapshot de awslabs/aidlc-workflows (MIT-0): ramas main (reglas v1) y v2 (2.0)

conocimiento/             El estudio de la implementación 2.0, leída archivo por archivo
├── LEEME.md              Por dónde empezar, y la respuesta a lo de las 3 fases contra las 5
├── 01 … 07               De las fuentes al método: cómo funciona, qué falta, v1 vs v2, cómo se trabaja
├── COMPARAR.md           La v1 y la v2 lado a lado, con los comandos para rehacer la comparación
└── diagramas/            Tres .drawio: un caso completo, el método en 11 páginas, la maquinaria

documento/                El entregable en curso: ocho capítulos en Markdown
└── entregable/           El .docx generado, y el build.py que lo arma

figuras/                  Las figuras del documento, en PNG y SVG
borradores/               Material previo: la presentación, el PDF v0.2.0, las plantillas
tabla-de-contenidos.md    La estructura acordada del documento

.claude/skills/humanizer/ Skill de redacción: la voz del documento y las marcas de IA prohibidas
```

## Estado

- **Fuentes descargadas y catalogadas.** Empezar por [`fuentes/FUENTES.md`](fuentes/FUENTES.md).
- **La implementación 2.0 está estudiada.** Siete documentos y tres diagramas en [`conocimiento/`](conocimiento/LEEME.md), leídos de los 33 archivos de etapa del repositorio oficial, no de su documentación.
- **La decisión de las 3 fases contra las 5 ya tiene respuesta.** No son dos metodologías: las 5 de la implementación son las 3 del paper con Inception partida en dos y una fase 0 de fontanería delante. El modelo mental del paper —la IA planifica, pregunta, y solo implementa tras validación humana— es literalmente el patrón que se repite en las 33 etapas. **La espina del paper que asume [`tabla-de-contenidos.md`](tabla-de-contenidos.md) se sostiene**, y la 2.0 entra como implementación de referencia. El detalle y la trampa que esconde la palabra «Inception», en [`conocimiento/LEEME.md`](conocimiento/LEEME.md).
- El documento en sí todavía no se redacta aquí. Existe un borrador previo cuya estructura va a cambiar: la sección de contexto institucional sale hacia material comercial, y la medición se muda al informe del caso piloto («documento hermano»).

## Cómo leerlo según a qué vengas

| Vengo a… | Empiezo por |
|---|---|
| entender qué es AI-DLC en diez minutos | [`conocimiento/diagramas/aidlc-v2-un-caso.drawio`](conocimiento/diagramas/aidlc-v2-un-caso.drawio) — un caso de principio a fin |
| aplicar el método | [`conocimiento/07-como-se-trabaja.md`](conocimiento/07-como-se-trabaja.md) |
| citar una fuente oficial | [`fuentes/FUENTES.md`](fuentes/FUENTES.md) |
| redactar el documento | [`tabla-de-contenidos.md`](tabla-de-contenidos.md) y [`documento/`](documento/) |

**Antes de citar un diagrama delante de un cliente**, leer [`conocimiento/diagramas/LEEME.md`](conocimiento/diagramas/LEEME.md): separa lo que sale verificado del repositorio de lo que es ilustración nuestra.
