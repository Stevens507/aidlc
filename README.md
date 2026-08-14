# Metodología AI-DLC — Grupo TX

Repositorio de trabajo para redactar el documento de metodología del área: cómo el equipo de IA Generativa aplica AI-DLC (AI-Driven Development Life Cycle), el método que AWS publicó en julio de 2025. El objetivo es un documento corto y legible: quien entra al equipo debería poder leerlo y entender el procedimiento completo sin que nadie se lo explique.

## Qué hay aquí

```
fuentes/                  Todo el material oficial de AWS, descargado el 14 ago 2026
├── FUENTES.md            Índice comentado: qué es cada fuente, fecha y URL original
├── paper/                Method Definition Paper (Raja SP, jul 2025) — PDF + texto extraído
├── especificacion/       Especificación AI-DLC Workflows 2.0 — PDF + texto extraído
├── blogs/                Los 3 blogs oficiales en inglés (jul 2025, nov 2025, may 2026)
├── blogs-regionales/     9 casos publicados en blogs oficiales de AWS Japón, Corea y China
└── repo-oficial/         Snapshot de awslabs/aidlc-workflows (MIT-0): ramas main (reglas v1) y v2 (implementación 2.0)

.claude/skills/humanizer/ Skill de redacción: la voz del documento y las marcas de IA prohibidas
```

## Estado

- Fuentes descargadas y catalogadas. Empezar por `fuentes/FUENTES.md`.
- El documento en sí todavía no se redacta aquí. Existe un borrador previo (índice comentado en Word) cuya estructura va a cambiar: la sección de contexto institucional sale hacia material comercial, y la medición se muda al informe del caso piloto («documento hermano»).
- Decisión pendiente antes de redactar: el paper original define 3 fases; la implementación 2.0 del repositorio trabaja con 5 fases y 33 etapas. Hay que elegir contra cuál versión se escribe el procedimiento (detalle en `fuentes/FUENTES.md`).
