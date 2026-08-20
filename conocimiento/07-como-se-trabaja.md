# Cómo se trabaja con AI-DLC — el método, sin la herramienta

Leído literalmente de los 33 archivos de etapa de [`../fuentes/repo-oficial/v2/core/aidlc-common/stages/`](../fuentes/repo-oficial/v2/core/aidlc-common/stages/). Esto describe **el trabajo**, no la maquinaria.

**Diagramas.** Dos, que se leen en orden distinto:

**1 · El caso** — [`diagramas/aidlc-v2-un-caso.drawio`](diagramas/aidlc-v2-un-caso.drawio) — *empieza por aquí*
Una página. Un módulo de fidelización que le falta a un CRM retail que ya está en producción, de la petición del cliente al rastro que queda en disco. Seis actos, con el texto literal que aparece en pantalla. Es la versión narrativa: se entiende sin conocer el framework.

**2 · El método** — [`diagramas/aidlc-v2-como-se-trabaja.drawio`](diagramas/aidlc-v2-como-se-trabaja.drawio) — *la referencia*
Once páginas, 346 cajas, 92 iconos vectoriales (Font Awesome y Carbon Pictograms, vía la librería de draw.io).

| # | Página | Qué responde |
|---|---|---|
| 1 | El ciclo completo, 33 etapas | El mapa entero, fase por fase — con la banda de las seis salvaguardas de brownfield |
| 2 | De cero, o sobre algo que ya existe | La bifurcación mayor |
| 3 | Los once caminos | Cuál eliges y qué cuesta cada uno |
| 4 | Qué hace que una etapa corra | Las condiciones reales |
| 5 | El ciclo de una etapa | El patrón que se repite 33 veces |
| 6 | Construcción, Bolt por Bolt | La fase que se comporta distinto |
| 7 | Los catorce oficios | Roles, niveles y momentos de decisión |
| 8 | Con qué método trabaja cada rol | Las 59 fichas de la biblioteca, y quién usa cuál |
| 9 | Qué queda escrito | Los 121 artefactos y la cadena de trazabilidad |
| 10 | Cómo se verifica y cómo aprende | Sensores, revisor, trazabilidad, y el bucle de aprendizaje |
| 11 | Cómo se adapta a tu organización | La cadena de reglas y la puerta de admisión |

La maquinaria (hooks, directivas, herramientas) está aparte, en [06](06-flujo-de-activacion.md) y en `diagramas/aidlc-v2-maquinaria.drawio`.

---

## Lo esencial, y dónde v2 se separa del paper

Esto es lo que no puede perderse de vista. Por eso va en una **franja fija, idéntica y en el mismo sitio, en las 12 páginas de los dos diagramas**.

### El modelo mental

Del blog fundacional de AWS, literal:

> «En su núcleo, AI-DLC opera haciendo que la IA inicie y dirija los flujos mediante un nuevo modelo mental: la IA **crea un plan**, hace **preguntas aclaratorias** para obtener contexto, e **implementa soluciones solo después de recibir validación humana**. Este patrón se repite rápidamente **para cada actividad del SDLC**.»
>
> — [blog-01](../fuentes/blogs/2025-07-31_ai-driven-development-life-cycle.md)

Más las dos dimensiones que el mismo texto pone por delante de todo:

- **Ejecución por IA con supervisión humana** — la IA planifica, pide aclaraciones y **difiere las decisiones críticas a las personas**, porque solo ellas tienen el contexto de negocio.
- **Colaboración dinámica del equipo** — mientras la IA hace lo rutinario, el equipo se junta a decidir en tiempo real.

Y el vocabulario que cambia: **bolt** en vez de sprint — ciclos de horas o días, no de semanas — y **unidad de trabajo** en vez de épica.

**El puente con la implementación:** ese bucle de cuatro pasos es exactamente el patrón que se repite en los 33 archivos de etapa — la sección siguiente. v2 no es otra cosa que ese bucle instanciado 33 veces. Dicho al revés: v2 no se alejó del paper, lo materializó.

### Las 3 fases del paper contra las 5 de v2

El paper describe tres. v2 implementa cinco. **Y v2 no documenta el mapeo en ningún sitio** — lo busqué en `docs/` y en `core/`; solo menciona «tres fases» de pasada, para decir que un agente cruza tres.

| Paper | v2 | Etapas |
|---|---|---|
| — | **0 · initialization** | 3 |
| **Inception** | **1 · ideation** + **2 · inception** | 7 + 9 |
| **Construction** | **3 · construction** | 7 |
| **Operations** | **4 · operation** | 7 |

Verificado en [`../fuentes/repo-oficial/v2/core/tools/aidlc-lib.ts`](../fuentes/repo-oficial/v2/core/tools/aidlc-lib.ts) línea 130 — la constante `PHASES` — y contando los directorios de `core/aidlc-common/stages/`: 3 + 7 + 9 + 7 + 7 = 33.

**La trampa está en la palabra «Inception».** En el paper abarca lo que en v2 son dos fases; en v2 nombra solo la segunda. Quien lea el paper y luego vea una pantalla que dice `INCEPTION` va a creer que está más avanzado de lo que está: le faltan por detrás las 7 etapas de ideación.

Y no es solo un desdoble, hay un **desplazamiento de frontera**: el paper pone los modelos de dominio en Construction, y v2 los tiene en inception — etapa 2.6.

Propósito de cada fase, según `docs/guide/04-phases-and-stages.md`:

| Fase | Propósito |
|---|---|
| 0 initialization | arrancar el espacio de trabajo: crear el directorio de documentos, detectar el proyecto e inicializar el estado. **Sin compuertas**, todo en una llamada determinista de menos de un segundo |
| 1 ideation | **validar la iniciativa**: capturar la intención, evaluar viabilidad, definir alcance, formar el equipo y conseguir aprobación para seguir |
| 2 inception | **elaborar los requisitos**: analizar el código, elicitar requisitos, diseñar la arquitectura, descomponer en unidades de trabajo y planificar la entrega |
| 3 construction | **construir la solución**: diseñar, implementar y probar, en rebanadas revisables |
| 4 operation | **desplegar y operar**: tuberías de despliegue, entornos, observabilidad y bucles de realimentación |

Las fronteras con **verificación automática de frontera de fase** son tres, no cuatro: ideación → inception, inception → construcción, construcción → operación. Initialization no tiene ninguna.

---

## El hallazgo al leer las 33

**Casi todas tienen la misma forma.** No es una lista de 33 procedimientos distintos: es **un patrón repetido 33 veces**, con el rol y el tema cambiando.

Extraído de los encabezados de pasos de cada archivo:

```
1  Cargar el rol que toca            ← Arquitecto, PM, QA, SRE…
2  Cargar el contexto previo         ← lo que ya se decidió
3  Generar preguntas de clarificación   ← la IA pregunta
4  Recoger y analizar las respuestas    ← el humano responde
5  Generar los artefactos               ← la IA produce
6  Traspaso de completitud
7  Presentar y pedir aprobación         ← el humano aprueba
```

Ese esqueleto aparece **literal** en 24 de las 33 etapas. Las demás lo amplían:

| Etapa | Qué añade |
|---|---|
| 2.3 Requisitos | 13 pasos. Añade evaluar profundidad, análisis de completitud en **seis dimensiones**, preguntas de seguimiento y confirmación del resumen |
| 2.6 Diseño de dominio | 9 pasos. Añade registrar decisiones de arquitectura (ADR) y la trazabilidad |
| 2.4 Historias de usuario | Se trabaja en **mob**: el PM lidera, y diseño, desarrollo y QA contribuyen en paralelo |
| 2.1 Ingeniería inversa | **Cadena**: uno escanea el código, otro sintetiza |
| 2.2 Descubrir prácticas | Borrador → revisión ciega → **entrevista** → integración → compuerta de afirmación |
| 3.5 Generación de código | Parte en dos: **planificar → aprobar el plan → generar** |
| 0.1–0.3 Arranque | Sin preguntas y sin compuerta: son mecánicas |

---

## Las 5 fases y lo que sale de cada una

| Fase | Etapas | La pregunta que responde | Lo que sale |
|---|---|---|---|
| **0 · Arranque** `initialization` | 3 | ¿dónde estamos? | El expediente abierto, y si hay código previo |
| **1 · Ideación** `ideation` | 7 | ¿vale la pena? | Intención escrita, mapa de interesados, alcance **con lo que queda fuera**, registro de riesgos, brief aprobado |
| **2 · Concepción** `inception` | 9 | ¿qué y cómo? | Requisitos, historias, modelo de dominio con sus ADR, el sistema partido en **Units**, plan de **Bolts** |
| **3 · Construcción** `construction` | 7 | construirlo | Código con pruebas, infraestructura como código, pipeline de CI |
| **4 · Operación** `operation` | 7 | mantenerlo vivo | Desplegado, con tableros, alarmas, SLO y runbooks |


> **Ojo con la traducción.** Llamo «Concepción» a la fase 2 porque en español se entiende, pero **en pantalla dice `INCEPTION`** — y esa palabra en el paper de AWS significa otra cosa más amplia. Ver [Las 3 fases del paper contra las 5 de v2](#las-3-fases-del-paper-contra-las-5-de-v2).

**Entre fase y fase se verifica la trazabilidad** antes de avanzar. La cadena que se comprueba:

```
Intención → Alcance → Requisitos → Diseños → Units → Código → Pruebas → Despliegue
```

Si falta un eslabón, se presenta el problema y **no se avanza**.

---

## Los tres momentos donde decide una persona

Más allá de las compuertas de cada etapa, hay tres decisiones que el método reserva explícitamente:

**1 · Al elegir el recorrido.** Se dice el número exacto de etapas y de compuertas — computado, no estimado — **antes** de empezar. Un bugfix son 7 de 33. Una funcionalidad completa, las 33.

**2 · Antes de generar código.** Parada dura, en todo modo de ejecución. Se presenta el plan y las instrucciones de prueba con una huella criptográfica; cualquier cambio posterior la invalida. El texto de la etapa lo dice sin rodeos: *«no infieras la aprobación de una continuación del bucle»*.

**3 · Al decidir la autonomía.** Se pregunta **una sola vez por proyecto**, y después de ver el primer Bolt terminado — no al principio, cuando aún no tienes evidencia.

---

## Cómo se responde a la IA

Cuando una etapa necesita saber algo, escribe las preguntas en un archivo y ofrece tres modos, intercambiables a media etapa:

- **Guíame** — una a una, en conversación
- **Yo edito el archivo** — las respondes por escrito y avisas
- **Conversemos** — hablas libre y la IA extrae las decisiones

En los tres, **el archivo es el registro autoritativo** y hay una confirmación consolidada antes de producir nada.

Y hay una sección entera del protocolo dedicada a **no asumir**:

> Por defecto preguntar, no asumir. Nunca proceder con ambigüedad. Banderas rojas: respuestas de una palabra a preguntas abiertas, «lo que tú creas», señales contradictorias, esquivar la pregunta.

Cuando defieres a la IA, te repregunta: *«quiero asegurarme de que el diseño refleje TUS prioridades»*.

También cruza tus respuestas buscando contradicciones — alcance («que sea simple» + peticiones enterprise), riesgo («la seguridad no importa» + datos sensibles), tecnología (offline-first + colaboración en tiempo real), plazo contra alcance. Cuando encuentra una, **presenta las dos respuestas lado a lado y no avanza hasta resolverla**.

---

## Construcción: la única fase que no va etapa por etapa

Va **Bolt por Bolt**. Un **Unit** es una parte del sistema que se entrega sola; un **Bolt** es el ciclo en que se construye.

1. **El primer Bolt es el esqueleto que camina** — atraviesa el sistema de punta a punta con lo mínimo. Va solo, y **siempre con compuerta**.
2. Tras aprobarlo, se pregunta una vez cómo siguen los demás: autónomo o revisando cada uno.
3. Los Bolts sin dependencia entre sí **corren en paralelo**.
4. **Si uno falla: se detiene, se conservan los que sí salieron, y te preguntan** — reintentar, saltar o abortar. Esto pasa **aunque hayas elegido autónomo**.
5. Construir y probar corre **una vez al final**, sobre todo lo construido.

**La autonomía tiene red:** el sistema no cree al agente cuando dice que terminó. Corre **el comando de prueba de tu proyecto**, y compara el archivo de pruebas contra su versión original para que nadie lo debilite y lo ponga verde.

> Y un límite que conviene saber: **el paralelismo solo existe si la etapa 2.7 partió el sistema en Units.** En un bugfix, un refactor o una prueba de concepto no hay Units — Construcción va de una sola pasada.

---

## Los catorce oficios

No son once herramientas: es **un rol que la IA adopta** según la etapa, con el conocimiento de ese oficio cargado.

| Rol | Lidera |
|---|---|
| Product Manager | 1.1 intención · 1.2 mercado · 1.4 alcance · 2.3 requisitos · 2.4 historias |
| Arquitecto | 1.3 viabilidad · 2.6 dominio · 2.7 Units · 2.8 contratos · 3.1–3.3 diseño y NFR |
| Delivery Manager | 1.5 equipo · 1.7 aprobación · 2.9 plan de entrega |
| Diseñador UX | 1.6 bocetos · 2.5 maquetas |
| Desarrollador | 2.1 leer el código existente · 3.5 generar código |
| QA | 3.6 construir y probar · 4.6 validar rendimiento |
| Plataforma AWS | 3.4 infraestructura · 4.2 entornos |
| Pipeline / Deploy | 2.2 prácticas · 3.7 CI · 4.1 y 4.3 despliegue |
| SRE | 4.4 observabilidad · 4.5 incidentes · 4.7 retroalimentación |
| Cumplimiento | **solo apoya** — aporta restricciones regulatorias |
| DevSecOps | **solo apoya** — amenazas y seguridad en el pipeline |
| **Revisor de arquitectura** | **no lidera: revisa** — cuestiona el resultado de 8 etapas de diseño y construcción |
| **Revisor de producto** | **no lidera: revisa** — cuestiona el resultado de 5 etapas de intención y requisitos |
| **Compositor** | **no lidera ninguna etapa** — es quien arma el plan a medida cuando respondes `compose`. Estima la entropía del encargo y propone la secuencia mínima suficiente. Lo despacha el orquestador, nunca una etapa |

Más dos revisores que no producen nada, solo cuestionan lo producido, y un composer que arma el recorrido a medida.

**Los agentes no se llaman entre sí.** Solo el orquestador reparte trabajo — eso mantiene el árbol de decisiones plano y auditable.

---


**Por qué catorce y no nueve:** nueve lideran etapas, dos **solo apoyan** aportando restricciones, dos **solo revisan** — y nunca ven cómo se construyó lo que revisan — y uno, el compositor, no aparece en ninguna etapa porque actúa antes de que exista el plan. Verificado contando `core/agents/` y los campos `lead_agent`, `support_agents` y `reviewer` de las 33 etapas.

---

## Lo que la IA no decide nunca

- Marcar una etapa como terminada
- Aprobar su propio trabajo en una compuerta
- Empezar a generar código sin el plan aprobado
- Convertir una corrección tuya en regla sin que lo confirmes
- Contradecir una regla de la organización

---

## El reparto, en una frase

> **Lo determinista** lo hace una herramienta · **lo que requiere conocimiento** lo hace un rol de la IA · **lo que requiere juicio** lo hace una persona.

Cuando el método duda de a cuál de las tres pertenece algo, lo manda a la persona.

---

# Los caminos

Lo anterior describe el patrón. Pero **el mismo método produce recorridos muy distintos**, y eso lo deciden dos ejes, no uno.

## Los dos ejes

**Eje 1 — el camino** elige qué etapas entran *en el plan*. Se decide al principio, y te dicen los números exactos antes de empezar.

**Eje 2 — la condición** decide, ya en marcha, si una etapa del plan *de verdad corre*.

> Por eso el número de etapas engaña. Un `feature` tiene **33 etapas en el plan, pero solo 8 son fijas** — las otras 22 se auto-seleccionan. El recorrido real está entre 11 y 33 etapas según el proyecto.

Contado del grafo compilado:

| Camino | Plan | Compuertas | Fijas | Condicionales | Esqueleto |
|---|---:|---:|---:|---:|---|
| `enterprise` | 33/33 | 30 | 8 | 22 | on |
| `feature` | 33/33 | 30 | 8 | 22 | on |
| `classic` *(el default implícito)* | 26/33 | 23 | 5 | 18 | on |
| `workshop` | 26/33 | 23 | 5 | 18 | on |
| `mvp` | 23/33 | 20 | 7 | 13 | on |
| `infra` | 13/33 | 10 | 1 | 9 | on |
| `express` | 10/33 | 7 | 3 | 4 | **off** |
| `security-patch` | 10/33 | 7 | 3 | 4 | **off** |
| `poc` | 8/33 | 5 | 4 | 1 | on |
| `refactor` | 8/33 | 5 | 3 | 2 | **off** |
| `bugfix` | 7/33 | 4 | 3 | 1 | **off** |

**Cómo se elige:** lo dices (`/aidlc bugfix`), lo infiere de palabras clave, o te propone uno a medida puntuando cinco componentes de incertidumbre — justificando cada etapa que incluye *y cada una que descarta*.

Con una regla de desambiguación: si escribes una palabra clave **y** más de cinco palabras de descripción, se ignora la palabra clave y se te ofrece el plan a medida. Evita que «arreglar el panel de monitoreo» se rutee a `bugfix` por accidente.

---

## La bifurcación mayor: de cero, o sobre algo que ya existe

**No la tomas tú.** La decide un escaneo determinista del directorio, en la etapa 0.2:

**Es código existente** si aparece *cualquiera* de: archivos fuente en 15 lenguajes reconocidos · configuración de framework · manifiesto con dependencias de aplicación · carpetas `src/ app/ lib/ pages/` · un `.gitmodules` con submódulos.

**Es de cero** solo si *ninguna* aparece. Un README, un LICENSE, un `.gitignore` o CI sin código **no** cuentan.

### Las cinco diferencias reales

| | Empezar de cero | Sobre algo que ya existe |
|---|---|---|
| **2.1 Ingeniería inversa** | se salta — no hay código que leer | **es lo primero.** Produce 9 artefactos: visión de negocio, arquitectura, estructura del código, API, inventario de componentes, stack, dependencias, evaluación de calidad |
| **2.2 Prácticas del equipo** | **te pregunta** — no hay evidencia que mirar | **las descubre** leyendo el repositorio. *La misma etapa comportándose al revés* |
| **Ideación** | donde más aporta: no hay nada, hay que decidir qué construir | normalmente se salta — no hay producto nuevo que descubrir |
| **Esqueleto que camina** | sí (`skeleton: on`) — atraviesa el sistema con lo mínimo para probar que el camino existe | no (`skeleton: off` en bugfix, refactor, security-patch). El sistema ya camina |
| **2.6 Diseño de dominio** | corre — todos los componentes son nuevos | se salta si solo modificas componentes que ya existen |

> **Un detalle que ahorra tiempo:** la ingeniería inversa **guarda lo que aprende por repositorio**. Si vuelves a trabajar sobre el mismo código, comprueba si el escaneo sigue vigente y te **ofrece reutilizarlo**. Solo re-escanea si está obsoleto, sin verificar, o no cubre lo que esta vez necesitas.

---

## Las condiciones, tal como están escritas

Esto es lo que hace que dos proyectos con el mismo camino recorran cosas distintas:

| Etapa | Corre si… |
|---|---|
| 1.2 Investigación de mercado | hay posicionamiento externo o decisión comprar-vs-construir. Se salta en herramientas internas |
| 1.3 Viabilidad | hay restricciones de integración, requisitos regulatorios o incertidumbre técnica seria |
| 1.5 Formación del equipo | la composición o capacidad importan. Se salta con un solo desarrollador |
| 1.6 Bocetos | hay interfaz de usuario. Para APIs produce diagramas de interacción |
| **2.1 Ingeniería inversa** | **el proyecto es código existente** |
| **2.2 Prácticas** | **siempre** — pero cambia de comportamiento según el caso |
| 2.4 Historias de usuario | hay funcionalidad de cara al usuario, varias personas, lógica compleja o trabajo entre equipos |
| 2.5 Maquetas refinadas | hay UI *y* hubo bocetos en ideación |
| **2.6 Diseño de dominio** | **hacen falta componentes nuevos. Se salta si solo modificas lo existente** |
| 2.8 Contratos | hay una frontera formal que fijar — más de una Unit que se hablen |
| 3.1 Diseño funcional | hay modelos de datos nuevos, lógica compleja o reglas de negocio |
| 3.2 Requisitos no funcionales | hacen falta requisitos de rendimiento, seguridad, escala, fiabilidad u observabilidad |
| 3.3 Diseño de los NFR | **corrió el 3.2.** Si aquel se saltó, este también |
| 3.4 Infraestructura | hay que mapear servicios o hacen falta recursos en la nube |
| 3.7 Pipeline de CI | hay que crearlo o modificarlo. **Se salta si el CI que hay ya sirve** |
| 4.1–4.7 Operación | cada una, si su necesidad concreta existe |

**Las tres condiciones que más cambian el viaje:**

1. **¿Hay código ya escrito?** — decide la ingeniería inversa y voltea el comportamiento de las prácticas.
2. **¿Componentes nuevos o modificaciones?** — decide el diseño de dominio, y con él media fase de concepción.
3. **¿Hay interfaz de usuario?** — decide bocetos, maquetas e historias.

**Quién evalúa estas condiciones:** no es un `if` en el código. Es **juicio de la IA sobre el contexto**, y por eso pasa por compuerta como todo lo demás. Cuando una etapa se salta queda registrado **con su razón**, y en ideación y concepción la compuerta puede ofrecerte **volver a meter** una etapa saltada — es la única circunstancia en que una compuerta ofrece una tercera opción.

---

## Qué queda escrito — los artefactos

**121 artefactos distintos, 128 producciones.** Nada se archiva al cerrar una fase: cada uno es el contexto con el que trabaja la etapa siguiente.

| Fase | Artefactos | Los que más pesan |
|---|---:|---|
| Ideación | 24 | Declaración de la intención · mapa de interesados · alcance · registro de riesgos · **brief de la iniciativa** |
| Concepción | 37 | **9 documentos del código existente** · requisitos · historias · catálogo de componentes · decisiones de arquitectura · **unidades de trabajo con su grafo de dependencias** · plan de Bolts |
| Construcción | 36 | Entidades · reglas de negocio · **5 grupos de requisitos no funcionales** y su diseño · especificación de infraestructura · **plan aprobado con huella** · instrucciones de prueba |
| Operación | 31 | Configuración de despliegue · runbook de reversión · inventario de entornos · tableros · alarmas · objetivos de servicio · matriz de escalamiento · análisis de costo y deriva |

### La trazabilidad no es un documento: la producen 8 etapas

El artefacto `traceability` lo escriben **historias de usuario, diseño de dominio, unidades, diseño funcional, requisitos no funcionales, su diseño, infraestructura y generación de código**. En construcción hay además una trazabilidad cruzada entre unidades.

Esa es la cadena que se verifica en cada frontera de fase:

```
intención → alcance → requisitos → diseños → unidades → código → pruebas → despliegue
```

Si un eslabón falta, no se avanza. **Es lo que responde a un auditor cuando pregunta de qué requisito salió una línea de código.**

> **El límite:** la cadena llega hasta el despliegue, pero **no hay vuelta atrás desde un commit**. v2 lo declara como *«pregunta de diseño abierta»* — no existe búsqueda inversa desde un commit arbitrario hasta su intención y su workflow. Para banca y sector público, eso no es un detalle menor.

---

## Cuando ya hay código — las seis salvaguardas

De `knowledge/aidlc-shared/brownfield.md`. Aplican a **cualquier etapa que modifique código o infraestructura existente**, y **no existen en un proyecto nuevo**.

> El riesgo cambia de naturaleza. De cero, el riesgo es **construir lo que no era**. Sobre algo que corre, es **romper lo que sí era**.

| Salvaguarda | Etapa | Qué hace |
|---|---|---|
| **Radio de impacto** | 2.1 · 3.5 | Identifica qué archivos y componentes se tocan y **quién depende de ellos aguas abajo**. Clasifica en bajo / medio / alto y lo presenta **antes** de proceder |
| **Vista previa del cambio** | cualquier modificación | Muestra el cambio exacto **antes** de aplicarlo. No hay escritura a ciegas |
| **Línea base de pruebas** | antes de 3.5 | Corre la suite **antes de tocar nada** y registra total, pasan, fallan, saltadas, cobertura |
| **Validación de pruebas** | 3.6 | Vuelve a correrla. **Los fallos nuevos son regresiones que introdujo el cambio.** Se arreglan antes de seguir |
| **Análisis de impacto** | 2.1 · 3.5 | Documenta qué APIs, componentes y dependencias quedan afectados |
| **Plan de reversión** | antes de 4.3 | Cómo deshacer el cambio. **Antes de desplegar**, no después del incidente |

**Las seis etapas donde cambia el comportamiento:** 2.1 ingeniería inversa · 2.2 prácticas (se invierte) · 2.6 diseño de dominio (se salta) · 3.5 generación de código · 3.6 construir y probar · 4.3 ejecutar el despliegue. En el diagrama van marcadas con un icono de edificio.

---

## La trazabilidad tiene un esquema de identificadores

De `knowledge/aidlc-shared/verification.md`. No es prosa: son **IDs estables** con prefijo fijo.

| Prefijo | Significa | Ejemplo |
|---|---|---|
| `FR{n}` / `FR{n}.{m}` | Requisito funcional | `FR1`, `FR1.2` |
| `NFR{n}` | Requisito no funcional de concepción | `NFR2` |
| `US{n}.{m}` | Historia de usuario | `US1.3` |
| `AC{n}.{m}.{seq}` | Criterio de aceptación | `AC1.3.2` |
| `U{n}` | Unidad de trabajo | `U1`, `u1-auth` |
| `BR{grupo}.{seq}` | Regla de negocio | `BR1.1` |

Y cada etapa que transforma requisitos, historias, diseños o código escribe un `traceability.json` con esta forma:

```json
{
  "stage": "functional-design",
  "unit": "u1-auth",
  "upstream_ids": ["AC1.1.1"],
  "coverage": [{ "id": "AC1.1.1", "status": "OK", "target": "BR1.1" }],
  "reverse":  [{ "id": "BR1.3", "status": "N/A", "target": "regla de validación técnica" }]
}
```

**`coverage` mira hacia arriba** (qué de lo anterior quedó cubierto) y **`reverse` hacia abajo** (qué de esto no viene de nada). Un sensor lo valida en cada escritura.

---

## Tres skills que cierran el ciclo

No son etapas: son comandos que se invocan cuando hacen falta.

| Skill | Qué produce |
|---|---|
| **`aidlc-outcomes-pack`** | Un **documento único de traspaso** al cerrar el workflow, con todo lo que el equipo necesita para operar y seguir construyendo el sistema **sin re-correr el workflow para recuperar el contexto** |
| **`aidlc-replay`** | Convierte el rastro de auditoría y los artefactos en **una historia legible**: qué se decidió, en qué orden y por qué. Para revisión asíncrona o para quien no estuvo |
| **`aidlc-session-cost`** | Vista determinista de lo consumido: duración, compuertas superadas, escrituras al diario, disparos de sensores, aprendizajes capturados |

`session-cost` tiene una disciplina que vale la pena copiar: *«esta skill **no cuenta nada por su cuenta**. No estima tokens, no recorre el árbol de artefactos, no lee el registro de auditoría. **Si un número no está en la salida de la herramienta, esta skill no lo inventa.**»*
