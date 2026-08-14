---
name: humanizer
description: Redactar y revisar prosa en español para el documento de metodología AI-DLC del área y cualquier otro entregable de texto del equipo. Aplicar siempre que se escriba, reescriba o revise contenido de esos documentos, para que el resultado suene a un autor humano concreto y no delate redacción por IA. No aplica a código ni a mensajes de chat.
---

# Humanizer — prosa de metodología que no suena a IA

## A qué suena este documento

El documento ya tiene una voz. Está en el borrador y es la referencia de calibración. Suena así:

> «El documento tiene dos lectores. Quien entra al equipo debería poder leerlo y entender el proceso completo sin que nadie se lo explique.»

> «Cómo se comprueba que el método funciona, sin depender de la percepción del equipo. Los datos viven en informes aparte; esta sección fija el procedimiento.»

> «Nunca métricas por persona.»

Rasgos de esa voz, en orden de importancia:

1. **Frase declarativa corta. Una idea por frase.** Si una frase necesita dos comas y un conector, casi siempre son dos frases.
2. **Dato concreto en lugar de calificativo.** «El tiempo de recuperación pasó de quince minutos a menos de tres», no «mejoró drásticamente los tiempos». Si no hay número, no se inventa un adverbio para taparlo: se dice lo que se sabe y punto.
3. **Decisiones en afirmativo, con dueño.** «Quién decide en los casos dudosos.» El documento dice qué se hace, quién lo hace y qué no se hace. Las renuncias explícitas («esto no lo hacemos», «el propio método excluye los sistemas simples») son parte de la voz: un texto de IA rara vez renuncia a algo.
4. **Registro impersonal latinoamericano, sin ceremonia.** Ni «usted deberá», ni tuteo, ni «nosotros creemos firmemente». Se admite primera persona del plural para decisiones del equipo: «conserva las fases y el vocabulario de AWS, y desarrolla lo que su material deja abierto».
5. **El vocabulario de AWS queda en inglés y sin comillas**: Inception, Construction, Operations, Mob Elaboration, Bolt, Unit, Intent. Se define una vez y se usa con naturalidad. No se traduce, no se pone en cursiva cada vez, no se re-explica.

## Marcas de IA — prohibidas

Cada una de estas, si aparece, se corrige. No son sugerencias.

**Relleno ceremonial.** «Es importante destacar», «cabe mencionar», «en el mundo actual», «en la era de la IA», «sin duda», «en definitiva», «en resumen». Se borran; la frase que queda casi siempre funciona sola.

**Tríadas y simetría.** «Claridad, velocidad y control.» «Más rápido, más barato y con mejor calidad.» La prosa humana es asimétrica: enumera dos cosas, o cuatro, o una lista de verdad. Si tres elementos aparecen en paralelo perfecto, quitar uno o romper el ritmo.

**El molde «no es X, es Y».** «No se trata de reemplazar personas, sino de potenciarlas.» Una vez por documento, quizás. Como patrón repetido, delata plantilla.

**Negrita sembrada.** Negrita en mitad de párrafos para «resaltar conceptos clave». En este documento la jerarquía la dan los títulos; el cuerpo va sin negritas salvo términos que se definen por primera vez.

**Listas donde va prosa.** Tres viñetas de una línea no son una sección. Si las ideas se siguen una a otra, van en párrafo. La viñeta se reserva para enumeraciones reales: requisitos, pasos, casos.

**Uniformidad estructural.** Todas las secciones con la misma cantidad de párrafos, todos los párrafos del mismo largo, cada sección abriendo con definición y cerrando con síntesis. Un autor humano es irregular: una sección importante es larga, una obvia despacha en dos líneas.

**Cierre motivacional.** Párrafos finales que resumen lo ya dicho o arengan («El futuro del desarrollo ya está aquí»). El documento termina cuando termina el contenido.

**Anglicismo de plantilla.** «Robusto», «empoderar», «apalancar», «sin fricciones», «accionable», «desafíos» como comodín, «clave» como adjetivo en cada página. También los falsos amigos de traducción automática: «asegurar que» por *ensure* (es «garantizar» o reformular), «soportar» por *support* (es «admitir» o «dar servicio a»).

**Vaguedad cuantificada.** «Mejora significativamente la productividad», «reduce considerablemente los errores». O hay número con fuente, o se afirma sin adverbio, o no se afirma.

**Gerundios y pasivas encadenados.** «Permitiendo optimizar los procesos, garantizando la calidad y facilitando la adopción.» Máximo un gerundio por frase, y con sujeto claro.

**Emojis, exclamaciones y preguntas retóricas** en títulos o cuerpo. Ninguno.

**Huir del verbo ser.** «Se erige como», «funciona como», «se posiciona como», «sirve como» donde alcanza con «es». La IA evita la cópula; el autor humano dice «el Bolt es la unidad de construcción» y sigue.

**Grandilocuencia de importancia.** «Marca un hito», «representa un cambio de paradigma», «juega un papel crucial en el panorama de», «deja un legado». Si algo importa, se muestra con el hecho; declararlo importante es no tener el hecho.

**Atribución fantasma.** «Los expertos señalan», «se considera que», «es ampliamente reconocido». O hay una fuente con nombre, o la afirmación es nuestra y se asume.

**Raya (—) como muletilla.** Una cada tanto, bien. Tres por párrafo convierten la prosa en apartes encadenados; se reescriben como frases.

**Cierre tipo esquema.** «A pesar de X, el método enfrenta desafíos…» como párrafo final de sección. Es el molde de conclusión de la IA; una sección técnica termina en su último hecho.

*Referencia externa: el catálogo «Signs of AI writing» de Wikipedia (los patrones que sus editores documentaron limpiando texto generado) coincide con esta lista y agrega las de formato: negrita sembrada, exceso de raya, title case en títulos, tablas donde va prosa. Ante la duda, esa guía es el estándar.*

## Cómo se escribe (no solo qué se evita)

- **Primero el hecho, después la consecuencia.** «AWS liberó la implementación como código abierto en diciembre de 2025. Eso permite X» — no al revés, no en abstracto.
- **Ritmo: variar el largo de las frases a propósito.** Tras dos o tres frases largas, una corta. La corta es la que se recuerda. «Nunca métricas por persona.»
- **Escribir como se le explicaría a la persona nueva del equipo**, en una conversación de trabajo. Prueba práctica: leer la frase en voz alta y preguntarse si alguien la diría así en una reunión. «Cabe destacar que el enfoque holístico…» no sobrevive a esa prueba.
- **Cortar el último 15–20 % de cada borrador.** La primera pasada siempre trae grasa: recapitulaciones, segundas explicaciones de lo mismo, frases puente. El texto corto no se logra escribiendo corto sino cortando.
- **Toda cifra lleva fuente y fecha** (el paper, un blog con fecha, el caso publicado). Lo que no tenga fuente se marca `[verificar]` y no se publica así.
- **Un término, un nombre.** Si en la sección 2 se llama «ciclo completo», no pasa a ser «flujo integral» en la 5. La elegancia por variación de sinónimos es marca de IA; la repetición del término correcto es marca de documentación técnica.

## Proceso de revisión

Tres pasadas, en este orden, sobre cualquier texto destinado al documento:

1. **Pasada de marcas.** Buscar y eliminar cada patrón de la lista de prohibidas. Es mecánica; no requiere criterio.
2. **Pasada de concreción.** Por cada afirmación, preguntar: ¿hay aquí un dato, nombre, fecha o ejemplo que la haga verificable? ¿Se puede reemplazar el calificativo por el hecho? ¿Sobrevive la frase a «¿lo diría así en una reunión?».
3. **Pasada de ritmo.** Leer de corrido. Marcar dónde el ojo patina: frases del mismo largo en serie, párrafos gemelos, conectores repetidos («además», «por otro lado», «asimismo»). Romper la simetría.

Al terminar, comparar el resultado contra los tres extractos de calibración del inicio. Si el texto nuevo desentona junto a ellos, no está listo.

## Reglas duras

- Nunca mencionar IA, modelos, prompts ni asistentes como autores o herramientas de redacción del documento. El documento habla de metodología con IA; no fue «escrito con IA» ante el lector.
- Nunca dejar meta-comentarios («como se mencionó anteriormente», «a continuación se detalla», «en esta sección veremos»). El título ya anuncia; el texto ejecuta.
- Ante la duda entre sonar inteligente y sonar claro, claro gana. Siempre.
