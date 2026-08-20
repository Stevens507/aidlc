# Los tres diagramas — qué es cada uno, y qué se puede citar

Los tres se abren con [draw.io](https://app.diagrams.net) (o la extensión de VS Code). Ninguno tiene dependencias: los iconos se cargan de la librería pública de draw.io.

| Archivo | Páginas | Para quién | Cuándo se usa |
|---|---|---|---|
| `aidlc-v2-un-caso.drawio` | 1 | quien nunca oyó hablar de AI-DLC | abrir una presentación |
| `aidlc-v2-como-se-trabaja.drawio` | 11 | quien va a aplicar el método | la referencia de trabajo |
| `aidlc-v2-maquinaria.drawio` | 4 | quien va a implementarlo | discusión técnica |

---

## 1 · Un caso de principio a fin

**Qué es.** Un módulo de fidelización por puntos que le falta a un CRM retail que ya está en producción, seguido desde la petición del cliente hasta el rastro auditable. Seis actos, de arriba abajo.

**Por qué ese caso.** Es el que más cosas activa. Es *brownfield*, así que se encienden las seis salvaguardas que un proyecto nuevo nunca ve. Toca dos módulos que ya funcionan — clientes y ventas — así que el radio de impacto sale alto de verdad. Y tiene reglas de negocio con aristas (caducidad, devoluciones, canje parcial) que hacen que el revisor tenga algo real que encontrar.

**El color no clasifica, señala quién manda:**

| | Significa |
|---|---|
| cálido | decide una persona |
| frío | trabaja la IA |
| verde | queda escrito en disco |
| rojo | parada dura |
| gris | ya existía antes de empezar |

---

## La franja — lo que se repite en las 12 páginas

Justo debajo del título, idéntica y en el mismo sitio en **todas** las páginas de los dos diagramas. Es el ancla: se puede entrar por cualquier página sin perder de vista qué es AI-DLC.

Lleva tres cosas:

**1 · El modelo mental.** `la IA planifica → pregunta por contexto → TÚ VALIDAS → la IA implementa`. El tercer paso va en cálido porque es el único que no hace la máquina. Es cita del blog fundacional de AWS, y el propio texto dice que **se repite para cada actividad del ciclo** — que es exactamente el patrón que aparece en los 33 archivos de etapa.

**2 · La cinta de fases.** Las 5 de v2 abajo, numeradas 0 a 4 con su número de etapas. Las 3 del paper arriba, **abarcando las que les tocan**. Así se ve sin explicarlo que la «Inception» del paper cubre dos fases de v2, y que `initialization` no existe en el paper.

**3 · El ancla de vocabulario.** `bolt` = ciclo de horas o días, no de semanas. `unidad de trabajo` = lo que antes era una épica.

Más la advertencia en rojo, que es la frase que más preguntas evita en una sala: **el paper describe 3 fases, v2 implementa 5, y la pantalla que dice INCEPTION no está donde el paper dice.** v2 no documenta ese mapeo en ninguna parte de su repositorio — lo verificamos buscando en `docs/` y `core/`.

En el diagrama del caso, además, **cada acto lleva su etiqueta de fase en los dos idiomas**: en qué fase de v2 cae, y a cuál de las 3 del paper corresponde.

---

## Lo que se puede citar, y lo que no

El diagrama mezcla dos cosas y conviene saber cuál es cuál antes de ponerlo delante de un cliente.

### Del repositorio, verificable

- La estructura de seis actos: escaneo → confirmación de alcance → preguntas → producción y revisión → construcción con salvaguardas → rastro.
- Los números del acto 1 — **33 etapas, 29 compuertas, 5 etapas por unidad de trabajo** — salen contados del grafo, y el framework los muestra *antes* de empezar. Que se muestren es lo que se afirma; los valores concretos dependen del camino.
- **`compose`** como tercera opción frente a confirmar o cambiar de camino, y que el plan a medida justifique tanto lo que entra como lo que descarta.
- El revisor recibe los artefactos pero **no el diario ni el plan** de quien los construyó.
- **LISTO / NO LISTO** como veredicto único, hasta dos reparaciones, y que en las etapas adversariales LISTO sea el veredicto al que se *falla en llegar*.
- El límite de **tres rondas de cambios** antes de que aparezca la opción de aceptar como está.
- Las **seis salvaguardas** de brownfield y que el plan se congele con una huella criptográfica.
- Las dos frases entre comillas sobre fondo amarillo son **texto literal del protocolo**: la de «por defecto preguntar, no asumir» y la de «no infieras la aprobación de una continuación del bucle».
- El **mapeo de fases**: v2 tiene 5 (`initialization`, `ideation`, `inception`, `construction`, `operation`), verificado en `core/tools/aidlc-lib.ts:130`, con 3+7+9+7+7 = 33 etapas. El paper tiene 3. El desdoble y el desplazamiento del diseño de dominio hacia inception son reales.
- Los **prefijos de trazabilidad** — `FR`, `NFR`, `US`, `AC`, `U`, `BR` — y que la cadena se recorra en los dos sentidos.

### Ilustrativo — plausible, pero inventado para el caso

Está marcado en el diagrama con una nota roja punteada, y conviene no citarlo como si fuera del framework:

- **Las cuatro preguntas de requisitos.** El framework dice «genera preguntas aclaratorias» y fija las seis dimensiones que debe cubrir; **no dice cuáles**. Las del diagrama son las que un analista razonable haría.
- **Los números de las pruebas** (847 / 841 / 6 / 73%, y 863 / 861 / 2 después). Que se tome una línea base antes y se valide después es del framework. Las cifras son de ejemplo.
- **La huella `sha256:4f2a9c…`**. El congelado del plan es real; el hash es de adorno.
- **Las reglas del negocio** — 1 punto por cada 10 de compra, caducidad a 12 meses, canje parcial con autorización. Son la respuesta *del cliente*, no del método.
- **El hallazgo del revisor** sobre el saldo negativo tras devolver una compra ya canjeada. Es el tipo de hueco que una revisión adversarial encuentra; el ejemplo es nuestro.
- **`FR3`, `US2.1`, `AC2.1.3`, `BR1.4`, `U2`** y la fecha del 12 de marzo. El esquema de identificadores es real; estos son de relleno.

### El límite que el diagrama declara

El último recuadro lo dice en rojo: la cadena de trazabilidad llega hasta el despliegue, **pero no hay vuelta atrás desde un commit**. No se puede tomar una línea de código en producción y remontar hasta el requisito que la originó. Va escrito a propósito — vale más que un cliente lo sepa por nosotros que lo descubra solo.

---

## Cómo está hecho

Generados con Python que escribe el XML de mxGraph directamente, con un verificador que comprueba **colisión entre todos los pares de cajas** antes de escribir. Ninguna de las tres tiene solapes.

Los iconos son `shape=image` apuntando a `icons.diagrams.net` — Font Awesome y IBM Carbon Pictograms. Son celdas propias, no imágenes de fondo, así que se pueden mover y redimensionar por separado sin tocar la caja.

**Nota práctica.** La página 1 de `aidlc-v2-como-se-trabaja.drawio` pesa unos 50 KB. Es válida y abre bien en draw.io, pero es demasiado grande para previsualizadores que cargan la página entera de una vez.
