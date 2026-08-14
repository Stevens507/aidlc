#!/usr/bin/env python3
"""Construye el documento de metodología sobre la plantilla del harness,
conservando portada, estilos, fuentes, encabezados y pie."""
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS = {'w': W}
ET.register_namespace('w', W)
ET.register_namespace('w14', 'http://schemas.microsoft.com/office/word/2010/wordml')
ET.register_namespace('r', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships')


def q(t):
    return '{%s}%s' % (W, t)


DOC = 'unpacked/word/document.xml'
tree = ET.parse(DOC)
root = tree.getroot()
body = root.find('w:body', NS)
kids = list(body)

# ---------------------------------------------------------------- portada
cover = kids[:18]          # imágenes, espaciadores y la tabla del título
sectPr = kids[-1]          # configuración de sección al final

REEMPLAZOS = {
    'El harness': 'Metodología AI-DLC',
    'Guía completa: qué es, cómo se usa, cómo se extiende':
        'Cómo construimos software con IA generativa',
    'Elaborado por: TX Intelligence': 'Elaborado por: Equipo de IA Generativa',
    'Fecha: 7 de agosto de 2026': 'Fecha: 14 de agosto de 2026',
    'Versión del documento: 2.1': 'Versión del documento: 1.0',
}
for el in cover:
    for t in el.iter(q('t')):
        if t.text and t.text.strip() in REEMPLAZOS:
            t.text = REEMPLAZOS[t.text.strip()]

# --------------------------------------------------------------- ayudantes
def xml(s):
    return ET.fromstring('<w:root xmlns:w="%s">%s</w:root>' % (W, s))


def runs(texto):
    """Convierte **negrita** en runs con w:b."""
    out, i = [], 0
    for parte in texto.split('**'):
        if not parte:
            i += 1
            continue
        if i % 2:
            out.append('<w:r><w:rPr><w:b w:val="1"/><w:bCs w:val="1"/></w:rPr>'
                       '<w:t xml:space="preserve">%s</w:t></w:r>' % escape(parte))
        else:
            out.append('<w:r><w:t xml:space="preserve">%s</w:t></w:r>' % escape(parte))
        i += 1
    return ''.join(out)


def h1(texto, salto=True):
    br = '<w:r><w:br w:type="page"/></w:r>' if salto else ''
    return ('<w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr>%s'
            '<w:r><w:t xml:space="preserve">%s</w:t></w:r></w:p>' % (br, escape(texto)))


def h2(texto):
    return ('<w:p><w:pPr><w:pStyle w:val="Heading2"/></w:pPr>'
            '<w:r><w:t xml:space="preserve">%s</w:t></w:r></w:p>' % escape(texto))


def h3(texto):
    return ('<w:p><w:pPr><w:pStyle w:val="Heading3"/></w:pPr>'
            '<w:r><w:t xml:space="preserve">%s</w:t></w:r></w:p>' % escape(texto))


def sub(texto):
    return ('<w:p><w:pPr><w:pStyle w:val="Subtitle"/></w:pPr>'
            '<w:r><w:t xml:space="preserve">%s</w:t></w:r></w:p>' % escape(texto))


def p(texto):
    return '<w:p>%s</w:p>' % runs(texto)


def vineta(texto):
    return ('<w:p><w:pPr><w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>'
            '<w:ind w:left="720" w:hanging="360"/></w:pPr>%s</w:p>' % runs(texto))


def figura(texto):
    return ('<w:p><w:pPr><w:spacing w:before="240" w:after="240"/><w:jc w:val="center"/></w:pPr>'
            '<w:r><w:rPr><w:i w:val="1"/><w:iCs w:val="1"/><w:color w:val="666666"/></w:rPr>'
            '<w:t xml:space="preserve">%s</w:t></w:r></w:p>' % escape(texto))


def cita(texto):
    return ('<w:p><w:pPr>'
            '<w:pBdr><w:left w:val="single" w:sz="18" w:space="12" w:color="2E86C1"/></w:pBdr>'
            '<w:spacing w:before="200" w:after="200"/>'
            '<w:ind w:left="720" w:right="720"/></w:pPr>'
            '<w:r><w:rPr><w:i w:val="1"/><w:iCs w:val="1"/></w:rPr>'
            '<w:t xml:space="preserve">%s</w:t></w:r></w:p>' % escape(texto))


def tabla(filas, anchos):
    grid = ''.join('<w:gridCol w:w="%d"/>' % a for a in anchos)
    trs = []
    for n, fila in enumerate(filas):
        tcs = []
        for celda, ancho in zip(fila, anchos):
            neg = '<w:rPr><w:b w:val="1"/><w:bCs w:val="1"/></w:rPr>' if n == 0 else ''
            cuerpo = ('<w:p><w:r>%s<w:t xml:space="preserve">%s</w:t></w:r></w:p>'
                      % (neg, escape(celda))) if n == 0 else '<w:p>%s</w:p>' % runs(celda)
            tcs.append('<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/></w:tcPr>%s</w:tc>'
                       % (ancho, cuerpo))
        cab = '<w:trPr><w:tblHeader/></w:trPr>' if n == 0 else ''
        trs.append('<w:tr>%s%s</w:tr>' % (cab, ''.join(tcs)))
    return ('<w:tbl><w:tblPr><w:tblStyle w:val="Table3"/>'
            '<w:tblW w:w="9360" w:type="dxa"/><w:tblLayout w:type="fixed"/></w:tblPr>'
            '<w:tblGrid>%s</w:tblGrid>%s</w:tbl>' % (grid, ''.join(trs)))


def espacio():
    return '<w:p/>'


# --------------------------------------------------------------- contenido
C = []

C += [h1('METODOLOGÍA AI-DLC')]
C += [sub('Cómo construimos software con IA generativa')]
C += [p('AI-DLC es la metodología de AWS para construir software con IA generativa, '
        'publicada en julio de 2025. El proceso coloca a la IA en el centro del desarrollo: '
        'en cada actividad, la IA analiza el contexto, propone un plan y pregunta lo que no sabe. '
        'El equipo corrige y aprueba; con esa aprobación, la IA implementa.')]
C += [p('Este documento describe cómo el equipo de IA Generativa aplica el método: qué trabajo '
        'entra al ciclo, con qué artefactos se trabaja, cómo se ordenan las fases, qué recorre '
        'un cambio y qué evidencia queda al final.')]

C += [h2('Contenido')]
C += [tabla([
    ['Sección', 'Contenido'],
    ['1. El método', 'Qué es AI-DLC y en qué se apoya'],
    ['2. Alcance', 'Qué trabajo recorre el ciclo completo y qué queda fuera'],
    ['3. Artefactos', 'Las seis piezas con las que trabaja el método'],
    ['4. Fases y rituales', 'Cómo se ordena el trabajo y cómo trabaja el equipo'],
    ['5. El flujo', 'Los nueve pasos, del Intent al despliegue'],
    ['6. Herramientas y skills', 'Qué capacidad cubre cada fase y con qué se resuelve hoy'],
    ['7. Gobernanza', 'Qué controla el proceso y qué evidencia queda'],
    ['8. Adopción', 'Cómo se incorpora el equipo al método'],
    ['Referencias', 'Fuentes del método y políticas aplicables'],
], [2600, 6760])]

# 1
C += [h1('1. EL MÉTODO')]
C += [p('AI-DLC es la metodología de AWS para construir software con IA generativa, publicada '
        'en julio de 2025. El proceso coloca a la IA en el centro del desarrollo: en cada '
        'actividad, la IA analiza el contexto, propone un plan y pregunta lo que no sabe. '
        'El equipo corrige y aprueba; con esa aprobación, la IA implementa. El mismo ciclo '
        'gobierna los requisitos, el diseño, el código, las pruebas y el despliegue.')]
C += [figura('[Figura 1 — La IA propone, el equipo decide]')]
C += [p('El método nace de un límite que a menudo afecta al equipo de desarrollo: el asistente '
        'que autocompleta hace tareas sueltas sin contexto del sistema, y la IA que construye '
        'sola entrega software que nadie puede defender ante un cliente. AI-DLC evita los dos '
        'extremos: la IA hace el trabajo, una persona toma cada decisión.')]

# 2
C += [h1('2. ALCANCE: CUÁNDO APLICA Y CUÁNDO NO')]
C += [p('El ciclo completo está pensado para sistemas con complejidad de arquitectura, '
        'decisiones de diseño que negociar y exigencias de escala, integración o cumplimiento. '
        'El trabajo simple no lo necesita.')]
C += [p('El alcance se decide por cambio, no por proyecto. Un cambio recorre el ciclo completo '
        'si cumple al menos una de estas condiciones:')]
C += [vineta('cambia un flujo de negocio;')]
C += [vineta('toca más de un componente;')]
C += [vineta('lleva más de dos días de trabajo;')]
C += [vineta('automatiza una decisión que afecta a una persona.')]
C += [p('Si no cumple ninguna, entra directo a la construcción con el ticket como única '
        'especificación.')]

# 3
C += [h1('3. ARTEFACTOS')]
C += [p('Un artefacto es una pieza concreta del ciclo: algo que se define, se aprueba y queda '
        'registrado. Son seis. Tres organizan el trabajo y tres son el producto de la construcción.')]
C += [h2('Los que organizan el trabajo')]
C += [tabla([
    ['Artefacto', 'Qué es'],
    ['Intent', 'Lo que se quiere lograr, dicho en términos de negocio. El equipo define el '
               'destino y la IA propone el camino.'],
    ['Unit', 'Una parte del sistema que se construye y se entrega por sí sola. Un Intent se '
             'descompone en Units; equivalen a los subdominios del diseño guiado por el dominio '
             'o a las épicas de Scrum.'],
    ['Bolt', 'El ciclo en que se construye un Unit. Es lo que en Scrum era el sprint, pero de '
             'horas o días en lugar de semanas. Un Unit puede necesitar varios Bolts.'],
], [2000, 7360])]
C += [h2('Los que produce la construcción')]
C += [tabla([
    ['Artefacto', 'Qué es'],
    ['Domain Design', 'La lógica de negocio de un Unit, sin decidir todavía la tecnología. '
                      'La IA modela con diseño guiado por el dominio: agregados, entidades, '
                      'objetos de valor, eventos, repositorios.'],
    ['Logical Design', 'El mismo diseño, ya resuelto para los requisitos no funcionales y con '
                       'los patrones de arquitectura que correspondan. Cada decisión queda '
                       'registrada en un ADR que una persona valida.'],
    ['Deployment Units', 'El paquete listo para desplegar: el código ejecutable, su '
                         'configuración y su infraestructura.'],
], [2000, 7360])]
C += [p('Un requisito no funcional describe qué tan bien hace el sistema lo que hace: cuánto '
        'tarda, cuánto aguanta, qué registra, qué protege.')]
C += [p('Ninguno de los seis se descarta al cerrar la fase. Todos quedan guardados y la IA los '
        'usa como memoria de contexto durante el resto del ciclo: el diseño recuerda lo que se '
        'decidió en los requisitos, y el despliegue recuerda lo que se decidió en el diseño.')]

# 4
C += [h1('4. FASES Y RITUALES')]
C += [p('La metodología ordena el trabajo en tres fases y define cómo trabaja el equipo dentro '
        'de cada una. Los rituales son esas sesiones de trabajo: el equipo revisa en vivo lo que '
        'la IA propuso y decide sobre la marcha.')]
C += [figura('[Figura 3 — El ciclo completo]')]
C += [h3('Inception: qué construir y por qué')]
C += [p('La IA propone las historias de usuario, los criterios de aceptación, los requisitos no '
        'funcionales, los riesgos y la descomposición del Intent en Units. El equipo revisa esa '
        'propuesta en vivo y corrige lo que está sobre-diseñado o lo que quedó corto. Ese ritual '
        'es la Mob Elaboration, y en él participan el Product Owner, los desarrolladores y la IA. '
        'La fase cierra con los Units aprobados y los Bolts sugeridos para construirlos.')]
C += [h3('Construction: cómo construirlo')]
C += [p('Cada Unit se construye en uno o más Bolts. La IA modela el dominio, resuelve los '
        'requisitos no funcionales y genera el código con sus pruebas. Los equipos intercambian '
        'las especificaciones de integración y deciden los patrones de arquitectura: es la Mob '
        'Construction. Para validar el resultado contra lo que se pidió, el Product Owner vuelve '
        'a la mesa en la Mob Testing. La fase cierra con Deployment Units probados.')]
C += [h3('Operations: mantenerlo vivo')]
C += [p('Despliegue, observabilidad e incidentes, con la IA analizando métricas, registros y '
        'trazas para anticipar anomalías. No tiene un ritual propio.')]
C += [h3('Los puntos de validación')]
C += [p('Ninguna fase avanza sola. En cada paso la IA presenta su propuesta y espera; el trabajo '
        'continúa cuando una persona la aprueba.')]

# 5
C += [h1('5. EL FLUJO')]
C += [p('El ciclo se recorre en nueve pasos, del Intent al sistema en producción.')]
C += [figura('[Figura 2 — El flujo: nueve pasos, tres fases]')]
C += [p('El recorrido empieza con un plan. La IA lee la intención de negocio y propone los pasos '
        'necesarios para llevarla a cabo; el equipo lo revisa, lo corrige y lo aprueba. Después '
        'la IA descompone cada paso en tareas más finas, bajo la misma revisión. Cada paso deja '
        'artefactos que el siguiente usa como contexto, y por eso el orden importa.')]
C += [h2('Sistema nuevo y sistema existente')]
C += [p('Los nueve pasos son los mismos en los dos casos. La diferencia está al principio de '
        'Construction: cuando el sistema ya existe, antes de modelar el dominio hay que elevar '
        'el código a un modelo.')]
C += [p('La IA lee el código y produce dos representaciones. El modelo estático muestra los '
        'componentes del dominio, sus responsabilidades y sus relaciones. El modelo dinámico '
        'muestra cómo esos componentes interactúan para resolver los casos de uso principales. '
        'Los desarrolladores y el Product Owner revisan y corrigen ambos modelos antes de '
        'continuar; con eso resuelto, el resto del recorrido es igual al de un sistema nuevo.')]

# 6
C += [h1('6. HERRAMIENTAS Y SKILLS')]
C += [p('El método no depende de una plataforma. Define qué capacidad hace falta en cada fase; '
        'cada proyecto la cubre con la herramienta que tenga.')]
C += [tabla([
    ['Fase', 'Qué capacidad hace falta', 'Con qué se cubre hoy', 'Estado'],
    ['Inception', 'Producir la spec en tres artefactos, cada uno con aprobación explícita',
     'Kiro', 'Propuesto'],
    ['Construction', 'Un asistente que cargue las reglas del repositorio, y una revisión con '
                     'veredicto antes de integrar',
     'Claude Code; Forge, orquestación de corridas autónomas con revisores y veredicto '
     'PASS/DENY/DENYSPEC', 'Real'],
    ['Operations', 'Verificaciones automáticas en cada cambio',
     'El CI de cada proyecto, con definiciones por stack', 'Real'],
], [1500, 3200, 3260, 1400])]
C += [p('La herramienta importa menos que lo que se le carga. Una skill es un paquete de '
        'estándares e instrucciones que la herramienta levanta sola cuando la tarea coincide, '
        'y con eso todos recorren el mismo camino sin tener que acordarse de nada.')]
C += [p('Ese mecanismo tiene un límite: funciona mientras alguien lo invoque. Por eso una regla '
        'que importa de verdad no se queda escrita, baja al CI o a un hook de git y actúa sin '
        'que nadie la llame.')]
C += [p('El resto se queda donde ya está. La metodología apunta y no duplica: cada herramienta '
        'mantiene su propia documentación.')]

# 7
C += [h1('7. GOBERNANZA')]
C += [p('El proceso deja constancia de quién decidió qué. Esa constancia es lo que responde a un '
        'auditor o al oficial de cumplimiento de un cliente.')]
C += [p('La política de gobernanza de IA del grupo fija la regla que gobierna todo lo demás:')]
C += [cita('Todo código generado por IA pasa revisión humana antes de integrarse. El merge lo '
           'ejecuta siempre una persona identificable.')]
C += [p('La responsabilidad de cada cambio recae siempre en una persona con nombre; ningún '
        'agente es Accountable de nada, nunca.')]
C += [p('Esa regla se sostiene sobre lo que el ciclo va dejando escrito. Los artefactos no se '
        'descartan al cerrar cada fase: la prueba lleva al código, el código al requisito y el '
        'requisito a la historia de usuario que lo originó. AWS señala esa trazabilidad de punta '
        'a punta como el requisito crítico para la revisión regulatoria, y es lo que permite '
        'reconstruir después por qué el sistema hace lo que hace.')]
C += [p('Lo que no salió bien también queda registrado. Toda escalación, incidente o sorpresa '
        'relevante produce un post-mortem corto con número correlativo. No es burocracia: sus '
        'conclusiones se convierten en cambios concretos, sea una regla, una skill o una '
        'verificación del CI.')]

# 8
C += [h1('8. ADOPCIÓN')]
C += [p('La inducción al método es la misma para todo el equipo, sin importar el proyecto en el '
        'que esté. El método no se estudia, se practica: los rituales se aprenden ejecutándolos '
        'sobre trabajo real.')]
C += [p('La inducción tiene cuatro piezas:')]
C += [vineta('**Este documento** — el vocabulario, el ciclo completo y por qué el método importa.')]
C += [vineta('**Las herramientas del proyecto** — instaladas y configuradas, con las reglas del '
             'repositorio cargadas.')]
C += [vineta('**El flujo de un cambio** — un caso recorrido de principio a fin, del Intent al '
             'despliegue.')]
C += [vineta('**El primer trabajo acompañado** — un cambio real, no un ejercicio, junto a alguien '
             'que ya recorrió el ciclo.')]
C += [p('La inducción termina cuando ese primer cambio llega a producción.')]

# Referencias
C += [h1('REFERENCIAS')]
C += [vineta('AWS, Method Definition Paper de AI-DLC, julio de 2025: fases, artefactos, rituales '
             'y los nueve pasos del flujo.')]
C += [vineta('AWS, blog «AI-Driven Development Life Cycle: Reimagining Software Engineering», '
             '31 de julio de 2025.')]
C += [vineta('AWS, blog «Building with AI-DLC using Amazon Q Developer», 29 de noviembre de 2025.')]
C += [vineta('AWS, blog «AI-Driven Development Lifecycle for Financial Services», 26 de mayo de '
             '2026: trazabilidad y controles en entornos regulados.')]
C += [vineta('AWS, repositorio awslabs/aidlc-workflows, licencia MIT-0. La implementación 2.0 '
             'reorganiza el ciclo en más fases y etapas que las descritas aquí.')]
C += [vineta('Política de gobernanza de IA del grupo, regla §13.5: revisión humana y merge humano.')]

# ------------------------------------------------------------- ensamblado
for el in kids[18:-1]:
    body.remove(el)

nuevos = []
for frag in C:
    for el in xml(frag):
        nuevos.append(el)

idx = list(body).index(sectPr)
for n, el in enumerate(nuevos):
    body.insert(idx + n, el)

tree.write(DOC, xml_declaration=True, encoding='UTF-8', method='xml')
print('paragraphs escritos:', len(nuevos))
