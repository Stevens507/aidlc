# La v1 y la v2, lado a lado

Las dos ramas de `awslabs/aidlc-workflows` están guardadas en este repositorio, así que la comparación se
puede rehacer sin clonar nada:

| Rama | Versión | Dónde | Archivos |
|---|---|---|---|
| `main` — la v1 | 1.0.1 | [`../fuentes/repo-oficial/main/`](../fuentes/repo-oficial/main/) | 294 |
| `v2` — la 2.0 GA | 2.6.54 | [`../aidlc-v2/`](../aidlc-v2/) | 3.185 |

Los dos snapshots son **completos**: el árbol entero de cada rama, sin quitar nada. Lo único que no traen es
el `.git`, así que para historial hay que clonar.

> **La trampa de quien clona.** La rama por defecto del repositorio de AWS es `main`, que es **la v1**, y
> GitHub sigue marcando la 1.0.1 como «Latest release» pese al GA de la 2.0
> (issue [#635](https://github.com/awslabs/aidlc-workflows/issues/635)). Quien clona sin especificar rama se
> lleva la v1 creyendo que se lleva lo último.

## Cómo comprobar cualquier afirmación

Contra los snapshots, con `grep` a secas:

```bash
# desde la raíz del repositorio
grep -ril "bolt" fuentes/repo-oficial/main/ | wc -l   # cuántos lo nombran en la v1
grep -ril "bolt" aidlc-v2/core/ | wc -l               # y en el núcleo de la v2

ls aidlc-v2/core/aidlc-common/stages/*/*.md | wc -l   # las 33 etapas
ls aidlc-v2/core/agents/*.md | wc -l                  # los 14 agentes
ls aidlc-v2/core/scopes/*.md | wc -l                  # los 11 scopes
```

Contra el repositorio vivo, si hace falta historial:

```bash
git clone -b v2 https://github.com/awslabs/aidlc-workflows
cd aidlc-workflows
git grep -ril "Bolt" origin/main | wc -l
git diff --stat origin/main v2
git show origin/main:aidlc-rules/aws-aidlc-rules/core-workflow.md
```

## Las diferencias verificadas

| Tema | v1 | v2 |
|---|---|---|
| Fases | 3, con Operations como marcador de 19 líneas | 5, con las 7 etapas de Operation implementadas |
| Etapas | 13 + 1 marcador | 33 |
| Agentes | — | 14: 9 lideran, 2 apoyan, 2 revisan, 1 compone |
| Bolt | 1 archivo lo nombra | 77 |
| Mob | 0 archivos | 1, la topología `mode: mob` |
| Documentos de entrada | Vision Document (16) + Technical Environment (25) | 0 — sustituidos por etapas |
| Proporcionalidad | profundidad adaptativa, decide el modelo | 11 scopes × 3 profundidades × 3 estrategias de prueba |
| Pasos del Plan de Nivel 1 | 7 de 9 | 9 de 9 |

**La conclusión que sorprende:** la v2 no se alejó del paper, se acercó. El vocabulario del paper que la v1
apenas usaba —Bolt, Mob— es el que la v2 implementa de verdad; y los documentos de entrada que la v1 exigía
por escrito desaparecieron porque ahora los sustituyen etapas que preguntan.

## El estudio completo

[LEEME](LEEME.md) · [01 fuentes](01-fuentes.md) · [02 cómo funciona](02-como-funciona.md) ·
[03 qué falta](03-que-falta.md) · [04 v1 vs v2](04-v1-vs-v2.md) ·
[05 mapa de la documentación](05-mapa-docs-v2.md) · [06 flujo de activación](06-flujo-de-activacion.md) ·
[07 cómo se trabaja](07-como-se-trabaja.md) · [diagramas](diagramas/LEEME.md)
