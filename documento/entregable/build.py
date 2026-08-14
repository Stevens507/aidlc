#!/usr/bin/env python3
"""Documento de metodología AI-DLC sobre la plantilla de TX Intelligence.

Conserva portada, estilos, fuentes embebidas, encabezado y pie, y replica el
formato del original: Poppins/Open Sans, azul 0084d5, marino 282d68, sangría
de 720, cuerpo justificado y tablas con cabecera marino y bordes grises.
"""
import os
import re
import shutil
import struct
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS = {'w': W}

# Registrar los prefijos tal como los declara la plantilla, para que el XML
# resultante conserve w:, wp:, a:, pic:, r: y no prefijos generados.
for _pref, _uri in [
    ('w', W),
    ('r', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'),
    ('wp', 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'),
    ('a', 'http://schemas.openxmlformats.org/drawingml/2006/main'),
    ('pic', 'http://schemas.openxmlformats.org/drawingml/2006/picture'),
    ('mc', 'http://schemas.openxmlformats.org/markup-compatibility/2006'),
    ('o', 'urn:schemas-microsoft-com:office:office'),
    ('m', 'http://schemas.openxmlformats.org/officeDocument/2006/math'),
    ('v', 'urn:schemas-microsoft-com:vml'),
    ('w10', 'urn:schemas-microsoft-com:office:word'),
    ('wne', 'http://schemas.microsoft.com/office/word/2006/wordml'),
    ('sl', 'http://schemas.openxmlformats.org/schemaLibrary/2006/main'),
    ('c', 'http://schemas.openxmlformats.org/drawingml/2006/chart'),
    ('w14', 'http://schemas.microsoft.com/office/word/2010/wordml'),
]:
    ET.register_namespace(_pref, _uri)

REPO = '/home/user/aidlc'
UNP = 'unpacked'
DOC = os.path.join(UNP, 'word/document.xml')

AZUL = '0084d5'      # títulos de nivel 1 y 3
MARINO = '282d68'    # títulos de nivel 2 y fondo de cabecera de tabla
BORDE = 'd9d9d9'
SANGRIA = 720        # media pulgada, como el cuerpo de la plantilla
ANCHO_TABLA = 9360


def q(t):
    return '{%s}%s' % (W, t)


# ------------------------------------------------------------------ figuras
FIGURAS = [
    ('figura1.png', os.path.join(REPO, 'figuras/fig1-mental-model.png')),
    ('figura2.png', os.path.join(REPO, 'figuras/fig2-nueve-pasos.png')),
    ('figura3.png', os.path.join(REPO, 'borradores/imagenes-presentacion/aws-paper_ciclo-completo.png')),
]
RID = {}
DIMS = {}


def registrar_figuras():
    rels_path = os.path.join(UNP, 'word/_rels/document.xml.rels')
    rels = open(rels_path, encoding='utf-8').read()
    usados = [int(n) for n in re.findall(r'Id="rId(\d+)"', rels)]
    siguiente = max(usados) + 1
    nuevas = []
    for nombre, origen in FIGURAS:
        shutil.copy(origen, os.path.join(UNP, 'word/media', nombre))
        with open(origen, 'rb') as fh:
            cab = fh.read(33)
        ancho_px, alto_px = struct.unpack('>II', cab[16:24])
        DIMS[nombre] = (ancho_px, alto_px)
        rid = 'rId%d' % siguiente
        RID[nombre] = rid
        nuevas.append(
            '<Relationship Id="%s" Type="http://schemas.openxmlformats.org/'
            'officeDocument/2006/relationships/image" Target="media/%s"/>' % (rid, nombre))
        siguiente += 1
    rels = rels.replace('</Relationships>', ''.join(nuevas) + '</Relationships>')
    open(rels_path, 'w', encoding='utf-8').write(rels)


# ---------------------------------------------------------------- ayudantes
def xml(s):
    return ET.fromstring(
        '<w:root xmlns:w="%s" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
        'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
        'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
        'xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">%s</w:root>' % (W, s))


def fuente(nombre):
    return ('<w:rFonts w:ascii="%s" w:cs="%s" w:eastAsia="%s" w:hAnsi="%s"/>'
            % (nombre, nombre, nombre, nombre))


def runs(texto, cara='Open Sans', tam=21, color=None):
    """Convierte **negrita** en runs con Open Sans SemiBold."""
    out, i = [], 0
    for parte in texto.split('**'):
        if not parte:
            i += 1
            continue
        f = fuente('Open Sans SemiBold' if i % 2 else cara)
        c = '<w:color w:val="%s"/>' % color if color else ''
        out.append('<w:r><w:rPr>%s%s<w:sz w:val="%d"/><w:szCs w:val="%d"/>'
                   '<w:rtl w:val="0"/></w:rPr><w:t xml:space="preserve">%s</w:t></w:r>'
                   % (f, c, tam, tam, escape(parte)))
        i += 1
    return ''.join(out)


def h1(texto):
    return ('<w:p><w:pPr><w:pStyle w:val="Heading1"/>'
            '<w:spacing w:after="120" w:before="240" w:line="240" w:lineRule="auto"/>'
            '<w:ind w:left="%d" w:firstLine="0"/><w:jc w:val="left"/>'
            '<w:rPr><w:color w:val="%s"/></w:rPr></w:pPr>'
            '<w:r><w:br w:type="page"/></w:r>'
            '<w:r><w:rPr>%s<w:b w:val="1"/><w:bCs w:val="1"/><w:color w:val="%s"/>'
            '<w:sz w:val="42"/><w:szCs w:val="42"/><w:rtl w:val="0"/></w:rPr>'
            '<w:t xml:space="preserve">%s</w:t></w:r></w:p>'
            % (SANGRIA, AZUL, fuente('Poppins'), AZUL, escape(texto)))


def h2(texto):
    return ('<w:p><w:pPr><w:pStyle w:val="Heading2"/>'
            '<w:spacing w:after="120" w:before="360" w:lineRule="auto"/>'
            '<w:ind w:left="%d" w:firstLine="0"/><w:jc w:val="left"/>'
            '<w:rPr><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr></w:pPr>'
            '<w:r><w:rPr>%s<w:color w:val="%s"/><w:sz w:val="28"/><w:szCs w:val="28"/>'
            '<w:rtl w:val="0"/></w:rPr><w:t xml:space="preserve">%s</w:t></w:r></w:p>'
            % (SANGRIA, fuente('Open Sans SemiBold'), MARINO, escape(texto)))


def h3(texto):
    return ('<w:p><w:pPr><w:pStyle w:val="Heading3"/>'
            '<w:spacing w:after="80" w:before="280" w:lineRule="auto"/>'
            '<w:ind w:left="%d" w:firstLine="0"/><w:jc w:val="left"/><w:rPr/></w:pPr>'
            '<w:r><w:rPr>%s<w:color w:val="%s"/><w:sz w:val="22"/><w:szCs w:val="22"/>'
            '<w:rtl w:val="0"/></w:rPr><w:t xml:space="preserve">%s</w:t></w:r></w:p>'
            % (SANGRIA, fuente('Open Sans SemiBold'), AZUL, escape(texto)))


def sub(texto):
    return ('<w:p><w:pPr><w:pStyle w:val="Subtitle"/>'
            '<w:spacing w:after="320" w:before="0" w:lineRule="auto"/>'
            '<w:ind w:left="%d" w:firstLine="0"/><w:jc w:val="left"/><w:rPr/></w:pPr>'
            '<w:r><w:rPr>%s<w:color w:val="666666"/><w:sz w:val="26"/><w:szCs w:val="26"/>'
            '<w:rtl w:val="0"/></w:rPr><w:t xml:space="preserve">%s</w:t></w:r></w:p>'
            % (SANGRIA, fuente('Open Sans'), escape(texto)))


def p(texto):
    return ('<w:p><w:pPr><w:spacing w:after="200" w:before="0" w:lineRule="auto"/>'
            '<w:ind w:left="%d" w:firstLine="0"/><w:jc w:val="both"/><w:rPr/></w:pPr>%s</w:p>'
            % (SANGRIA, runs(texto)))


def vineta(texto):
    return ('<w:p><w:pPr><w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>'
            '<w:spacing w:after="80" w:before="0" w:lineRule="auto"/>'
            '<w:ind w:left="1080" w:hanging="360"/><w:jc w:val="left"/><w:rPr/></w:pPr>%s</w:p>'
            % runs(texto))


def cita(texto):
    return ('<w:p><w:pPr>'
            '<w:pBdr><w:left w:val="single" w:sz="18" w:space="10" w:color="%s"/></w:pBdr>'
            '<w:spacing w:after="200" w:before="200" w:lineRule="auto"/>'
            '<w:ind w:left="1080" w:right="720" w:firstLine="0"/><w:jc w:val="left"/>'
            '<w:rPr/></w:pPr>'
            '<w:r><w:rPr>%s<w:color w:val="%s"/><w:sz w:val="22"/><w:szCs w:val="22"/>'
            '<w:rtl w:val="0"/></w:rPr><w:t xml:space="preserve">%s</w:t></w:r></w:p>'
            % (AZUL, fuente('Open Sans SemiBold'), MARINO, escape(texto)))


def figura(nombre, leyenda, ancho_pulgadas=5.6):
    ancho_px, alto_px = DIMS[nombre]
    cx = int(ancho_pulgadas * 914400)
    cy = int(cx * alto_px / ancho_px)
    dibujo = (
        '<w:p><w:pPr><w:spacing w:after="80" w:before="240" w:lineRule="auto"/>'
        '<w:ind w:left="%d" w:firstLine="0"/><w:jc w:val="center"/><w:rPr/></w:pPr>'
        '<w:r><w:rPr><w:rtl w:val="0"/></w:rPr><w:drawing>'
        '<wp:inline distB="0" distT="0" distL="0" distR="0">'
        '<wp:extent cx="%d" cy="%d"/><wp:effectExtent b="0" l="0" r="0" t="0"/>'
        '<wp:docPr id="%d" name="%s"/>'
        '<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        '<pic:pic><pic:nvPicPr><pic:cNvPr id="0" name="%s"/>'
        '<pic:cNvPicPr preferRelativeResize="0"/></pic:nvPicPr>'
        '<pic:blipFill><a:blip r:embed="%s"/><a:srcRect b="0" l="0" r="0" t="0"/>'
        '<a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
        '<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="%d" cy="%d"/></a:xfrm>'
        '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>'
        '</pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>'
        % (SANGRIA, cx, cy, abs(hash(nombre)) % 9000 + 100, nombre, nombre,
           RID[nombre], cx, cy))
    pie = ('<w:p><w:pPr><w:spacing w:after="240" w:before="0" w:lineRule="auto"/>'
           '<w:ind w:left="%d" w:firstLine="0"/><w:jc w:val="center"/><w:rPr/></w:pPr>'
           '<w:r><w:rPr>%s<w:i w:val="1"/><w:iCs w:val="1"/><w:color w:val="666666"/>'
           '<w:sz w:val="18"/><w:szCs w:val="18"/><w:rtl w:val="0"/></w:rPr>'
           '<w:t xml:space="preserve">%s</w:t></w:r></w:p>'
           % (SANGRIA, fuente('Open Sans'), escape(leyenda)))
    return dibujo + pie


def _celda(texto, ancho, cabecera):
    fondo = MARINO if cabecera else 'ffffff'
    cara = 'Open Sans SemiBold' if cabecera else 'Open Sans'
    color = '<w:color w:val="ffffff"/>' if cabecera else ''
    if cabecera:
        cuerpo = ('<w:r><w:rPr>%s%s<w:sz w:val="18"/><w:szCs w:val="18"/>'
                  '<w:rtl w:val="0"/></w:rPr><w:t xml:space="preserve">%s</w:t></w:r>'
                  % (fuente(cara), color, escape(texto)))
    else:
        cuerpo = runs(texto, cara='Open Sans', tam=18)
    return ('<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/>'
            '<w:shd w:fill="%s" w:val="clear"/><w:vAlign w:val="center"/></w:tcPr>'
            '<w:p><w:pPr><w:spacing w:after="40" w:before="40" w:line="240" w:lineRule="auto"/>'
            '<w:ind w:left="60" w:right="60" w:firstLine="0"/><w:jc w:val="left"/>'
            '<w:rPr/></w:pPr>%s</w:p></w:tc>' % (ancho, fondo, cuerpo))


def tabla(filas, anchos):
    grid = ''.join('<w:gridCol w:w="%d"/>' % a for a in anchos)
    trs = []
    for n, fila in enumerate(filas):
        cab = n == 0
        tcs = ''.join(_celda(c, a, cab) for c, a in zip(fila, anchos))
        trpr = ('<w:trPr><w:cantSplit w:val="0"/><w:tblHeader w:val="1"/></w:trPr>'
                if cab else '<w:trPr><w:cantSplit w:val="0"/></w:trPr>')
        trs.append('<w:tr>%s%s</w:tr>' % (trpr, tcs))
    b = ''.join('<w:%s w:color="%s" w:space="0" w:sz="4" w:val="single"/>' % (x, BORDE)
                for x in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'))
    return ('<w:tbl><w:tblPr><w:tblStyle w:val="Table2"/>'
            '<w:tblW w:w="%d" w:type="dxa"/><w:jc w:val="left"/>'
            '<w:tblInd w:w="%d" w:type="dxa"/><w:tblBorders>%s</w:tblBorders>'
            '<w:tblLayout w:type="fixed"/><w:tblLook w:val="0000"/></w:tblPr>'
            '<w:tblGrid>%s</w:tblGrid>%s</w:tbl>'
            % (ANCHO_TABLA, SANGRIA, b, grid, ''.join(trs)))


def espacio():
    return ('<w:p><w:pPr><w:spacing w:after="0" w:before="0"/>'
            '<w:ind w:left="%d" w:firstLine="0"/><w:rPr/></w:pPr></w:p>' % SANGRIA)


# ---------------------------------------------------------------- contenido
def contenido():
    C = []
    C += [h1('METODOLOGÍA AI-DLC')]
    C += [sub('Cómo construimos software con IA generativa')]
    C += [p('AI-DLC es la metodología de AWS para construir software con IA generativa, '
            'publicada en julio de 2025. El proceso coloca a la IA en el centro del desarrollo: '
            'en cada actividad, la IA analiza el contexto, propone un plan y pregunta lo que no '
            'sabe. El equipo corrige y aprueba; con esa aprobación, la IA implementa.')]
    C += [p('Este documento describe cómo el equipo de IA Generativa aplica el método: qué '
            'trabajo entra al ciclo, con qué artefactos se trabaja, cómo se ordenan las fases, '
            'qué recorre un cambio y qué evidencia queda al final.')]
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
    ], [2800, 6560])]

    C += [h1('1. EL MÉTODO')]
    C += [p('AI-DLC es la metodología de AWS para construir software con IA generativa, '
            'publicada en julio de 2025. El proceso coloca a la IA en el centro del desarrollo: '
            'en cada actividad, la IA analiza el contexto, propone un plan y pregunta lo que no '
            'sabe. El equipo corrige y aprueba; con esa aprobación, la IA implementa. El mismo '
            'ciclo gobierna los requisitos, el diseño, el código, las pruebas y el despliegue.')]
    C += [figura('figura1.png', 'Figura 1. La IA propone, el equipo decide.')]
    C += [p('El método nace de un límite que a menudo afecta al equipo de desarrollo: el '
            'asistente que autocompleta hace tareas sueltas sin contexto del sistema, y la IA '
            'que construye sola entrega software que nadie puede defender ante un cliente. '
            'AI-DLC evita los dos extremos: la IA hace el trabajo, una persona toma cada decisión.')]

    C += [h1('2. ALCANCE: CUÁNDO APLICA Y CUÁNDO NO')]
    C += [p('El ciclo completo está pensado para sistemas con complejidad de arquitectura, '
            'decisiones de diseño que negociar y exigencias de escala, integración o '
            'cumplimiento. El trabajo simple no lo necesita.')]
    C += [p('El alcance se decide por cambio, no por proyecto. Un cambio recorre el ciclo '
            'completo si cumple al menos una de estas condiciones:')]
    C += [vineta('cambia un flujo de negocio;')]
    C += [vineta('toca más de un componente;')]
    C += [vineta('lleva más de dos días de trabajo;')]
    C += [vineta('automatiza una decisión que afecta a una persona.')]
    C += [espacio()]
    C += [p('Si no cumple ninguna, entra directo a la construcción con el ticket como única '
            'especificación.')]

    C += [h1('3. ARTEFACTOS')]
    C += [p('Un artefacto es una pieza concreta del ciclo: algo que se define, se aprueba y '
            'queda registrado. Son seis. Tres organizan el trabajo y tres son el producto de '
            'la construcción.')]
    C += [h2('Los que organizan el trabajo')]
    C += [tabla([
        ['Artefacto', 'Qué es'],
        ['Intent', 'Lo que se quiere lograr, dicho en términos de negocio. El equipo define el '
                   'destino y la IA propone el camino.'],
        ['Unit', 'Una parte del sistema que se construye y se entrega por sí sola. Un Intent se '
                 'descompone en Units; equivalen a los subdominios del diseño guiado por el '
                 'dominio o a las épicas de Scrum.'],
        ['Bolt', 'El ciclo en que se construye un Unit. Es lo que en Scrum era el sprint, pero '
                 'de horas o días en lugar de semanas. Un Unit puede necesitar varios Bolts.'],
    ], [2200, 7160])]
    C += [h2('Los que produce la construcción')]
    C += [tabla([
        ['Artefacto', 'Qué es'],
        ['Domain Design', 'La lógica de negocio de un Unit, sin decidir todavía la tecnología. '
                          'La IA modela con diseño guiado por el dominio: agregados, entidades, '
                          'objetos de valor, eventos, repositorios.'],
        ['Logical Design', 'El mismo diseño, ya resuelto para los requisitos no funcionales y '
                           'con los patrones de arquitectura que correspondan. Cada decisión '
                           'queda registrada en un ADR que una persona valida.'],
        ['Deployment Units', 'El paquete listo para desplegar: el código ejecutable, su '
                             'configuración y su infraestructura.'],
    ], [2200, 7160])]
    C += [espacio()]
    C += [p('Un requisito no funcional describe qué tan bien hace el sistema lo que hace: cuánto '
            'tarda, cuánto aguanta, qué registra, qué protege.')]
    C += [p('Ninguno de los seis se descarta al cerrar la fase. Todos quedan guardados y la IA '
            'los usa como memoria de contexto durante el resto del ciclo: el diseño recuerda lo '
            'que se decidió en los requisitos, y el despliegue recuerda lo que se decidió en el '
            'diseño.')]

    C += [h1('4. FASES Y RITUALES')]
    C += [p('La metodología ordena el trabajo en tres fases y define cómo trabaja el equipo '
            'dentro de cada una. Los rituales son esas sesiones de trabajo: el equipo revisa en '
            'vivo lo que la IA propuso y decide sobre la marcha.')]
    C += [figura('figura3.png', 'Figura 2. El ciclo completo: roles, fases y artefactos.', 5.4)]
    C += [h3('Inception: qué construir y por qué')]
    C += [p('La IA propone las historias de usuario, los criterios de aceptación, los requisitos '
            'no funcionales, los riesgos y la descomposición del Intent en Units. El equipo '
            'revisa esa propuesta en vivo y corrige lo que está sobre-diseñado o lo que quedó '
            'corto. Ese ritual es la Mob Elaboration, y en él participan el Product Owner, los '
            'desarrolladores y la IA. La fase cierra con los Units aprobados y los Bolts '
            'sugeridos para construirlos.')]
    C += [h3('Construction: cómo construirlo')]
    C += [p('Cada Unit se construye en uno o más Bolts. La IA modela el dominio, resuelve los '
            'requisitos no funcionales y genera el código con sus pruebas. Los equipos '
            'intercambian las especificaciones de integración y deciden los patrones de '
            'arquitectura: es la Mob Construction. Para validar el resultado contra lo que se '
            'pidió, el Product Owner vuelve a la mesa en la Mob Testing. La fase cierra con '
            'Deployment Units probados.')]
    C += [h3('Operations: mantenerlo vivo')]
    C += [p('Despliegue, observabilidad e incidentes, con la IA analizando métricas, registros '
            'y trazas para anticipar anomalías. No tiene un ritual propio.')]
    C += [h3('Los puntos de validación')]
    C += [p('Ninguna fase avanza sola. En cada paso la IA presenta su propuesta y espera; el '
            'trabajo continúa cuando una persona la aprueba.')]

    C += [h1('5. EL FLUJO')]
    C += [p('El ciclo se recorre en nueve pasos, del Intent al sistema en producción.')]
    C += [figura('figura2.png', 'Figura 3. Los nueve pasos, agrupados en las tres fases.')]
    C += [p('El recorrido empieza con un plan. La IA lee la intención de negocio y propone los '
            'pasos necesarios para llevarla a cabo; el equipo lo revisa, lo corrige y lo aprueba. '
            'Después la IA descompone cada paso en tareas más finas, bajo la misma revisión. '
            'Cada paso deja artefactos que el siguiente usa como contexto, y por eso el orden '
            'importa.')]
    C += [h2('Sistema nuevo y sistema existente')]
    C += [p('Los nueve pasos son los mismos en los dos casos. La diferencia está al principio de '
            'Construction: cuando el sistema ya existe, antes de modelar el dominio hay que '
            'elevar el código a un modelo.')]
    C += [p('La IA lee el código y produce dos representaciones. El modelo estático muestra los '
            'componentes del dominio, sus responsabilidades y sus relaciones. El modelo dinámico '
            'muestra cómo esos componentes interactúan para resolver los casos de uso '
            'principales. Los desarrolladores y el Product Owner revisan y corrigen ambos '
            'modelos antes de continuar; con eso resuelto, el resto del recorrido es igual al de '
            'un sistema nuevo.')]

    C += [h1('6. HERRAMIENTAS Y SKILLS')]
    C += [p('El método no depende de una plataforma. Define qué capacidad hace falta en cada '
            'fase; cada proyecto la cubre con la herramienta que tenga.')]
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
    ], [1400, 3100, 3460, 1400])]
    C += [espacio()]
    C += [p('La herramienta importa menos que lo que se le carga. Una skill es un paquete de '
            'estándares e instrucciones que la herramienta levanta sola cuando la tarea '
            'coincide, y con eso todos recorren el mismo camino sin tener que acordarse de nada.')]
    C += [p('Ese mecanismo tiene un límite: funciona mientras alguien lo invoque. Por eso una '
            'regla que importa de verdad no se queda escrita, baja al CI o a un hook de git y '
            'actúa sin que nadie la llame.')]
    C += [p('El resto se queda donde ya está. La metodología apunta y no duplica: cada '
            'herramienta mantiene su propia documentación.')]

    C += [h1('7. GOBERNANZA')]
    C += [p('El proceso deja constancia de quién decidió qué. Esa constancia es lo que responde '
            'a un auditor o al oficial de cumplimiento de un cliente.')]
    C += [p('La política de gobernanza de IA del grupo fija la regla que gobierna todo lo demás:')]
    C += [cita('Todo código generado por IA pasa revisión humana antes de integrarse. El merge '
               'lo ejecuta siempre una persona identificable.')]
    C += [p('La responsabilidad de cada cambio recae siempre en una persona con nombre; ningún '
            'agente es Accountable de nada, nunca.')]
    C += [p('Esa regla se sostiene sobre lo que el ciclo va dejando escrito. Los artefactos no '
            'se descartan al cerrar cada fase: la prueba lleva al código, el código al requisito '
            'y el requisito a la historia de usuario que lo originó. AWS señala esa trazabilidad '
            'de punta a punta como el requisito crítico para la revisión regulatoria, y es lo '
            'que permite reconstruir después por qué el sistema hace lo que hace.')]
    C += [p('Lo que no salió bien también queda registrado. Toda escalación, incidente o '
            'sorpresa relevante produce un post-mortem corto con número correlativo. No es '
            'burocracia: sus conclusiones se convierten en cambios concretos, sea una regla, '
            'una skill o una verificación del CI.')]

    C += [h1('8. ADOPCIÓN')]
    C += [p('La inducción al método es la misma para todo el equipo, sin importar el proyecto en '
            'el que esté. El método no se estudia, se practica: los rituales se aprenden '
            'ejecutándolos sobre trabajo real.')]
    C += [p('La inducción tiene cuatro piezas:')]
    C += [vineta('**Este documento** — el vocabulario, el ciclo completo y por qué el método '
                 'importa.')]
    C += [vineta('**Las herramientas del proyecto** — instaladas y configuradas, con las reglas '
                 'del repositorio cargadas.')]
    C += [vineta('**El flujo de un cambio** — un caso recorrido de principio a fin, del Intent '
                 'al despliegue.')]
    C += [vineta('**El primer trabajo acompañado** — un cambio real, no un ejercicio, junto a '
                 'alguien que ya recorrió el ciclo.')]
    C += [espacio()]
    C += [p('La inducción termina cuando ese primer cambio llega a producción.')]

    C += [h1('REFERENCIAS')]
    C += [vineta('AWS, Method Definition Paper de AI-DLC, julio de 2025: fases, artefactos, '
                 'rituales y los nueve pasos del flujo.')]
    C += [vineta('AWS, blog «AI-Driven Development Life Cycle: Reimagining Software '
                 'Engineering», 31 de julio de 2025.')]
    C += [vineta('AWS, blog «Building with AI-DLC using Amazon Q Developer», 29 de noviembre '
                 'de 2025.')]
    C += [vineta('AWS, blog «AI-Driven Development Lifecycle for Financial Services», 26 de '
                 'mayo de 2026: trazabilidad y controles en entornos regulados.')]
    C += [vineta('AWS, repositorio awslabs/aidlc-workflows, licencia MIT-0. La implementación '
                 '2.0 reorganiza el ciclo en más fases y etapas que las descritas aquí.')]
    C += [vineta('Política de gobernanza de IA del grupo, regla §13.5: revisión humana y merge '
                 'humano.')]
    return C


# ----------------------------------------------------------------- montaje
registrar_figuras()

tree = ET.parse(DOC)
root = tree.getroot()
body = root.find('w:body', NS)
kids = list(body)
cover = kids[:18]
sectPr = kids[-1]

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

for el in kids[18:-1]:
    body.remove(el)

nuevos = [el for frag in contenido() for el in xml(frag)]
idx = list(body).index(sectPr)
for n, el in enumerate(nuevos):
    body.insert(idx + n, el)

tree.write(DOC, xml_declaration=True, encoding='UTF-8', method='xml')
print('bloques escritos:', len(nuevos), '| figuras:', list(RID.items()))
