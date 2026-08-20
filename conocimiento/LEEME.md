# El estudio de la implementación 2.0

Lectura de `awslabs/aidlc-workflows` rama `v2`, archivo por archivo, hecha el 19 y 20 de agosto de 2026. Responde a la pregunta que el README dejaba abierta: **el paper define 3 fases y la implementación trabaja con 5 — ¿contra cuál se escribe el procedimiento?**

## La respuesta corta

La v2 **no reemplaza al paper: lo materializa.** El modelo mental del paper —la IA planifica, pregunta, y solo implementa tras validación humana— es exactamente el patrón que se repite en los 33 archivos de etapa de la v2. Las 5 fases no son una metodología distinta; son las 3 del paper con la primera partida en dos y una fase 0 de fontanería añadida delante.

| Paper | Implementación 2.0 | Etapas |
|---|---|---|
| — | `initialization` | 3 |
| **Inception** | `ideation` + `inception` | 7 + 9 |
| **Construction** | `construction` | 7 |
| **Operations** | `operation` | 7 |

Verificado en [`../fuentes/repo-oficial/v2/core/tools/aidlc-lib.ts`](../fuentes/repo-oficial/v2/core/tools/aidlc-lib.ts) línea 130, constante `PHASES`, y contando los directorios de `core/aidlc-common/stages/`: 3 + 7 + 9 + 7 + 7 = 33.

**La trampa está en la palabra «Inception».** En el paper abarca lo que en la 2.0 son dos fases; en la 2.0 nombra solo la segunda. Quien lea el paper y luego vea una pantalla que dice `INCEPTION` va a creer que está más avanzado de lo que está. Y hay un desplazamiento de frontera además del desdoble: el paper pone los modelos de dominio en Construction, la 2.0 los tiene en inception. **La propia documentación de AWS no declara este mapeo en ninguna parte** — lo buscamos en su `docs/` y en su `core/`.

Consecuencia para el documento del área: la espina del paper que ya asume [`../tabla-de-contenidos.md`](../tabla-de-contenidos.md) **se sostiene**. La 2.0 entra como implementación de referencia, no como estructura alternativa.

## Por dónde empezar

| # | Documento | Qué responde |
|---|---|---|
| | [Diagrama: un caso completo](diagramas/aidlc-v2-un-caso.drawio) | **Empezar por aquí.** Un módulo que le falta a un CRM en producción, de la petición al rastro auditable |
| 01 | [Fuentes](01-fuentes.md) | Qué se leyó, dónde está cada cosa, y la línea de tiempo de versiones |
| 02 | [Cómo funciona](02-como-funciona.md) | La arquitectura: motor, director de orquesta, y la frontera de compilación |
| 03 | [Qué falta](03-que-falta.md) | Qué está hecho, qué está vacío y qué está roto en la 2.0 |
| 04 | [v1 vs v2](04-v1-vs-v2.md) | La comparación verificada, con los comandos para reproducirla |
| 05 | [Mapa de la documentación](05-mapa-docs-v2.md) | Índice de los 95 archivos de documentación de AWS |
| 06 | [Flujo de activación](06-flujo-de-activacion.md) | Qué enciende qué: ganchos, directivas, herramientas |
| 07 | [Cómo se trabaja](07-como-se-trabaja.md) | **El método**, leído de los 33 archivos de etapa. Agnóstico a la herramienta |

Los tres diagramas y qué se puede citar de cada uno: [`diagramas/LEEME.md`](diagramas/LEEME.md).

## Una advertencia de versiones

**El estudio se hizo contra la 2.6.18; el snapshot que guarda este repo en [`../fuentes/repo-oficial/v2/`](../fuentes/repo-oficial/v2/) es la 2.6.2.** La estructura es idéntica —33 etapas, 14 agentes, 5 fases, el `PHASES` en la misma línea— así que todas las citas de estos documentos se sostienen contra el snapshot. La diferencia que sí importa:

| | 2.6.2 (el snapshot) | 2.6.18 (el estudio) |
|---|---|---|
| Scopes | 9 | **11** — añade `aidlc-classic` y `aidlc-express` |

Si un número de estos documentos no cuadra con el snapshot, esa es la razón. Para reproducir contra la versión estudiada: `git clone -b v2 https://github.com/awslabs/aidlc-workflows`.
