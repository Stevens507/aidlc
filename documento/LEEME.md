# El documento: cómo se edita y cómo se genera

**El Markdown manda el contenido. `base.docx` manda el formato.** Se edita el `.md` y se regenera el Word; la portada, los estilos, las fuentes, el encabezado y el pie no se tocan nunca a mano.

```
documento/
├── 00-portada.md … 09-referencias.md    ← aquí se escribe
└── entregable/
    ├── base.docx                        ← la plantilla. NO se edita
    ├── build.py                          markdown → docx
    ├── extraer.py                        docx → markdown (solo para sembrar)
    └── Metodologia-AI-DLC-v1.0.docx       ← lo que se entrega. NO se edita
```

## Para cambiar algo

Editas el capítulo que toque y ejecutas:

```bash
cd documento/entregable
python build.py
```

Eso reconstruye `Metodologia-AI-DLC-v1.0.docx` desde cero conservando el formato. **No abras el `.docx` para editarlo:** el siguiente `build.py` te borraría el cambio. Todo va al Markdown.

## Cómo se escribe

| En el Markdown | Sale como |
|---|---|
| `# TÍTULO` | capítulo, empieza en página nueva, Poppins azul 42 |
| `## Título` | sección, Open Sans SemiBold marino 28 |
| `### Título` | subsección, azul 22 |
| `#### Título` | subtítulo gris bajo el título |
| texto suelto | párrafo justificado, sangría 720 |
| `**negrita**` | Open Sans SemiBold |
| `- item` | viñeta |
| `> texto` | cita con barra azul a la izquierda |
| `---` | línea de aire |

**Tablas.** Markdown normal; la primera fila es la cabecera, en marino con letra blanca. Los anchos van en un comentario justo encima, en veinteavos de punto:

```markdown
<!-- anchos: 2800,6560 -->
| Sección | Contenido |
|---|---|
| 1. El método | Qué es AI-DLC y en qué se apoya |
```

Si no pones el comentario, reparte el ancho a partes iguales.

**Figuras.** El ancho, en pulgadas, va en el atributo de título:

```markdown
![Figura 1. La IA propone, el equipo decide.](image4.png "4.2")
```

Para **añadir una imagen nueva**: pon el `.png` en `figuras/` y referencialo por su nombre de archivo. `build.py` lo mete en el paquete y le crea la relación. Si el nombre no está en `figuras/`, lo busca dentro de `base.docx` — así siguen funcionando las tres que ya venían. Para **reemplazar** una existente, basta con dejar un archivo con ese mismo nombre en `figuras/`: gana el de `figuras/`.

## Los capítulos

Se ordenan por el número del nombre y se concatenan. Para añadir uno, crea `10-loquesea.md` y aparecerá al final. Para reordenar, renombra.

`00-portada.md` **no contiene la portada** — esa vive en `base.docx` y se conserva intacta. Contiene lo que va después: el índice de contenidos.

## Si hay que volver a sembrar desde un Word

Solo si alguien edita el `.docx` a mano y hay que recuperar ese texto:

```bash
python extraer.py "ruta/al/documento.docx"
```

**Sobrescribe todos los `NN-*.md`.** Es la operación inversa y se usa una vez, no en el día a día.

## Qué está verificado

El ciclo `docx → markdown → docx` conserva **las 1.709 palabras, cero líneas distintas**. El paquete resultante tiene las mismas 38 entradas, las 10 imágenes byte a byte, y `styles.xml`, `fontTable.xml`, `header1.xml`, `footer1.xml` y `numbering.xml` idénticos al original.

## Lo que falta por escribir

El documento son **1.709 palabras**: la estructura y los párrafos-resumen, no el contenido desarrollado. Hay material listo para llenarlo en [`../conocimiento/`](../conocimiento/LEEME.md) — el mapeo de fases, los once caminos y su guía de elección, dónde aparece el código en cada uno, las seis salvaguardas y los tres diagramas.

Y una fila concreta pendiente: en la tabla de la sección 6, **Kiro figura como `Real`**. Convendría revisarla contra lo que salió de la primera corrida real.
