#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Markdown -> docx, sobre la plantilla de TX Intelligence.

El contenido manda desde `documento/*.md`. El formato manda desde `base.docx`:
portada, estilos, fuentes embebidas, encabezado, pie y numeracion salen de ahi
sin tocarse. Este script solo sustituye el cuerpo.

    python build.py

Dialecto del Markdown, el mismo que escribe extraer.py:

    # Titulo            capitulo, empieza en pagina nueva
    ## Titulo           seccion
    ### Titulo          subseccion
    #### Titulo         subtitulo gris bajo el titulo
    texto               parrafo justificado; **negrita** funciona
    - item              vineta
    > texto             cita con barra azul a la izquierda
    ![Leyenda](fig.png "4.2")     figura centrada; el ancho va en pulgadas
    <!-- anchos: 2800,6560 -->    anchos de la tabla que viene debajo
    | a | b |           tabla; la primera fila es cabecera
    ---                 linea en blanco de separacion

Para anadir una figura nueva: pon el .png en `figuras/` y referencialo por su
nombre de archivo. Si no esta ahi, se busca dentro del docx base.
"""
import io
import os
import re
import shutil
import struct
import zipfile
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS = {'w': W}

for _p, _u in [
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
    ET.register_namespace(_p, _u)

AQUI = os.path.dirname(os.path.abspath(__file__))
DOCUMENTO = os.path.dirname(AQUI)
REPO = os.path.dirname(DOCUMENTO)
FIGURAS = os.path.join(REPO, 'figuras')
BASE = os.path.join(AQUI, 'base.docx')
SALIDA = os.path.join(AQUI, 'Metodologia-AI-DLC-v1.0.docx')
UNP = os.path.join(AQUI, '.unpacked')
DOC = os.path.join(UNP, 'word/document.xml')

PORTADA = 18         # elementos 0..17 del cuerpo: no se tocan
AZUL = '0084d5'
MARINO = '282d68'
BORDE = 'd9d9d9'
SANGRIA = 720
ANCHO_TABLA = 9360


def q(t):
    return '{%s}%s' % (W, t)


# ---------------------------------------------------------------- ayudantes
def xml(s):
    return ET.fromstring(
        '<w:root xmlns:w="%s" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
        'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
        'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
        'xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">%s</w:root>' % (W, s))


def fuente(n):
    return ('<w:rFonts w:ascii="%s" w:cs="%s" w:eastAsia="%s" w:hAnsi="%s"/>' % (n, n, n, n))


def runs(texto, cara='Open Sans', tam=21, color=None):
    """**negrita** se convierte en runs con Open Sans SemiBold."""
    out = []
    for i, parte in enumerate(texto.split('**')):
        if not parte:
            continue
        f = fuente('Open Sans SemiBold' if i % 2 else cara)
        c = '<w:color w:val="%s"/>' % color if color else ''
        out.append('<w:r><w:rPr>%s%s<w:sz w:val="%d"/><w:szCs w:val="%d"/>'
                   '<w:rtl w:val="0"/></w:rPr><w:t xml:space="preserve">%s</w:t></w:r>'
                   % (f, c, tam, tam, escape(parte)))
    return ''.join(out)


def h1(t):
    return ('<w:p><w:pPr><w:pStyle w:val="Heading1"/>'
            '<w:spacing w:after="120" w:before="240" w:line="240" w:lineRule="auto"/>'
            '<w:ind w:left="%d" w:firstLine="0"/><w:jc w:val="left"/>'
            '<w:rPr><w:color w:val="%s"/></w:rPr></w:pPr>'
            '<w:r><w:br w:type="page"/></w:r>'
            '<w:r><w:rPr>%s<w:b w:val="1"/><w:bCs w:val="1"/><w:color w:val="%s"/>'
            '<w:sz w:val="42"/><w:szCs w:val="42"/><w:rtl w:val="0"/></w:rPr>'
            '<w:t xml:space="preserve">%s</w:t></w:r></w:p>'
            % (SANGRIA, AZUL, fuente('Poppins'), AZUL, escape(t)))


def h2(t):
    return ('<w:p><w:pPr><w:pStyle w:val="Heading2"/>'
            '<w:spacing w:after="120" w:before="360" w:lineRule="auto"/>'
            '<w:ind w:left="%d" w:firstLine="0"/><w:jc w:val="left"/>'
            '<w:rPr><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr></w:pPr>'
            '<w:r><w:rPr>%s<w:color w:val="%s"/><w:sz w:val="28"/><w:szCs w:val="28"/>'
            '<w:rtl w:val="0"/></w:rPr><w:t xml:space="preserve">%s</w:t></w:r></w:p>'
            % (SANGRIA, fuente('Open Sans SemiBold'), MARINO, escape(t)))


def h3(t):
    return ('<w:p><w:pPr><w:pStyle w:val="Heading3"/>'
            '<w:spacing w:after="80" w:before="280" w:lineRule="auto"/>'
            '<w:ind w:left="%d" w:firstLine="0"/><w:jc w:val="left"/><w:rPr/></w:pPr>'
            '<w:r><w:rPr>%s<w:color w:val="%s"/><w:sz w:val="22"/><w:szCs w:val="22"/>'
            '<w:rtl w:val="0"/></w:rPr><w:t xml:space="preserve">%s</w:t></w:r></w:p>'
            % (SANGRIA, fuente('Open Sans SemiBold'), AZUL, escape(t)))


def sub(t):
    return ('<w:p><w:pPr><w:pStyle w:val="Subtitle"/>'
            '<w:spacing w:after="320" w:before="0" w:lineRule="auto"/>'
            '<w:ind w:left="%d" w:firstLine="0"/><w:jc w:val="left"/><w:rPr/></w:pPr>'
            '<w:r><w:rPr>%s<w:color w:val="666666"/><w:sz w:val="26"/><w:szCs w:val="26"/>'
            '<w:rtl w:val="0"/></w:rPr><w:t xml:space="preserve">%s</w:t></w:r></w:p>'
            % (SANGRIA, fuente('Open Sans'), escape(t)))


def p(t):
    return ('<w:p><w:pPr><w:spacing w:after="200" w:before="0" w:lineRule="auto"/>'
            '<w:ind w:left="%d" w:firstLine="0"/><w:jc w:val="both"/><w:rPr/></w:pPr>%s</w:p>'
            % (SANGRIA, runs(t)))


def vineta(t):
    return ('<w:p><w:pPr><w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>'
            '<w:spacing w:after="80" w:before="0" w:lineRule="auto"/>'
            '<w:ind w:left="1080" w:hanging="360"/><w:jc w:val="left"/><w:rPr/></w:pPr>%s</w:p>'
            % runs(t))


def cita(t):
    return ('<w:p><w:pPr>'
            '<w:pBdr><w:left w:val="single" w:sz="18" w:space="10" w:color="%s"/></w:pBdr>'
            '<w:spacing w:after="200" w:before="200" w:lineRule="auto"/>'
            '<w:ind w:left="1080" w:right="720" w:firstLine="0"/><w:jc w:val="left"/>'
            '<w:rPr/></w:pPr>'
            '<w:r><w:rPr>%s<w:color w:val="%s"/><w:sz w:val="22"/><w:szCs w:val="22"/>'
            '<w:rtl w:val="0"/></w:rPr><w:t xml:space="preserve">%s</w:t></w:r></w:p>'
            % (AZUL, fuente('Open Sans SemiBold'), MARINO, escape(t.replace('**', ''))))


def espacio():
    return ('<w:p><w:pPr><w:spacing w:after="0" w:before="0"/>'
            '<w:ind w:left="%d" w:firstLine="0"/><w:rPr/></w:pPr></w:p>' % SANGRIA)


# ----------------------------------------------------------------- figuras
RID, DIMS = {}, {}


def png_tam(ruta):
    with open(ruta, 'rb') as fh:
        cab = fh.read(33)
    return struct.unpack('>II', cab[16:24])


def registrar_figuras(nombres):
    """Deja cada figura lista en el paquete y devuelve su rId.

    Si el nombre existe en `figuras/`, se copia de ahi (asi se anaden nuevas y
    se reemplazan las viejas). Si no, se usa la que ya trae el docx base.
    """
    rels_path = os.path.join(UNP, 'word/_rels/document.xml.rels')
    rels = io.open(rels_path, encoding='utf-8').read()
    siguiente = max(int(n) for n in re.findall(r'Id="rId(\d+)"', rels)) + 1
    nuevas, origen_de = [], {}

    for nombre in nombres:
        propio = os.path.join(FIGURAS, nombre)
        destino = os.path.join(UNP, 'word/media', nombre)
        if os.path.exists(propio):
            shutil.copy(propio, destino)
            origen_de[nombre] = 'figuras/'
        elif os.path.exists(destino):
            origen_de[nombre] = 'base.docx'
        else:
            raise SystemExit('falta la figura %s: ponla en figuras/' % nombre)
        DIMS[nombre] = png_tam(destino)
        ya = re.search(r'Id="(rId\d+)"[^>]*Target="media/%s"' % re.escape(nombre), rels)
        if ya:
            RID[nombre] = ya.group(1)
        else:
            RID[nombre] = 'rId%d' % siguiente
            nuevas.append('<Relationship Id="rId%d" Type="http://schemas.openxmlformats.org/'
                          'officeDocument/2006/relationships/image" Target="media/%s"/>'
                          % (siguiente, nombre))
            siguiente += 1
    if nuevas:
        rels = rels.replace('</Relationships>', ''.join(nuevas) + '</Relationships>')
        io.open(rels_path, 'w', encoding='utf-8').write(rels)
    return origen_de


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


# ------------------------------------------------------------------ tablas
def _celda(texto, ancho, cabecera):
    fondo = MARINO if cabecera else 'ffffff'
    if cabecera:
        cuerpo = ('<w:r><w:rPr>%s<w:color w:val="ffffff"/><w:sz w:val="18"/>'
                  '<w:szCs w:val="18"/><w:rtl w:val="0"/></w:rPr>'
                  '<w:t xml:space="preserve">%s</w:t></w:r>'
                  % (fuente('Open Sans SemiBold'), escape(texto.replace('**', ''))))
    else:
        cuerpo = runs(texto, cara='Open Sans', tam=18)
    return ('<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/>'
            '<w:shd w:fill="%s" w:val="clear"/><w:vAlign w:val="center"/></w:tcPr>'
            '<w:p><w:pPr><w:spacing w:after="40" w:before="40" w:line="240" w:lineRule="auto"/>'
            '<w:ind w:left="60" w:right="60" w:firstLine="0"/><w:jc w:val="left"/>'
            '<w:rPr/></w:pPr>%s</w:p></w:tc>' % (ancho, fondo, cuerpo))


def tabla(filas, anchos):
    n = len(filas[0])
    if len(anchos) != n or not all(anchos):
        anchos = [ANCHO_TABLA // n] * n
    grid = ''.join('<w:gridCol w:w="%d"/>' % a for a in anchos)
    trs = []
    for i, fila in enumerate(filas):
        cab = i == 0
        fila = (fila + [''] * n)[:n]
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


# ------------------------------------------------------------- el markdown
RE_FIG = re.compile(r'^!\[(?P<ley>.*?)\]\((?P<src>[^)\s]+)(?:\s+"(?P<ancho>[\d.]+)")?\)$')
RE_ANCHOS = re.compile(r'^<!--\s*anchos:\s*([\d,\s]+)-->$')


def capitulos():
    fs = sorted(f for f in os.listdir(DOCUMENTO)
                if re.match(r'^\d\d-.*\.md$', f))
    if not fs:
        raise SystemExit('no hay capitulos .md en %s' % DOCUMENTO)
    return fs


def parsear(lineas):
    """Markdown -> lista de ('tipo', datos). Sin tocar XML todavia."""
    bloques, i, anchos = [], 0, None
    while i < len(lineas):
        l = lineas[i].rstrip()
        if not l.strip():
            i += 1
            continue
        m = RE_ANCHOS.match(l.strip())
        if m:
            anchos = [int(x) for x in m.group(1).replace(' ', '').split(',') if x]
            i += 1
            continue
        if l.startswith('|'):                      # tabla
            filas = []
            while i < len(lineas) and lineas[i].lstrip().startswith('|'):
                celdas = [c.strip() for c in lineas[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-{2,}:?', c) for c in celdas):
                    filas.append(celdas)
                i += 1
            bloques.append(('tabla', (filas, anchos or [])))
            anchos = None
            continue
        m = RE_FIG.match(l.strip())
        if m:
            bloques.append(('figura', (m.group('src'), m.group('ley'),
                                       float(m.group('ancho') or 5.6))))
            i += 1
            continue
        if l.startswith('#### '):
            bloques.append(('sub', l[5:].strip()))
        elif l.startswith('### '):
            bloques.append(('h3', l[4:].strip()))
        elif l.startswith('## '):
            bloques.append(('h2', l[3:].strip()))
        elif l.startswith('# '):
            bloques.append(('h1', l[2:].strip()))
        elif l.startswith('> '):
            bloques.append(('cita', l[2:].strip()))
        elif l.startswith('- '):
            bloques.append(('vineta', l[2:].strip()))
        elif l.strip() == '---':
            bloques.append(('espacio', None))
        else:
            bloques.append(('p', l.strip()))
        i += 1
    return bloques


CONSTRUCTOR = {'h1': h1, 'h2': h2, 'h3': h3, 'sub': sub,
               'p': p, 'vineta': vineta, 'cita': cita}


def contenido():
    """Lee los .md y devuelve los fragmentos XML del cuerpo."""
    todos = []
    for f in capitulos():
        ls = io.open(os.path.join(DOCUMENTO, f), encoding='utf-8').read().split('\n')
        todos += parsear(ls)

    figs = [b[1][0] for b in todos if b[0] == 'figura']
    origen = registrar_figuras(figs) if figs else {}

    frags = []
    for tipo, dato in todos:
        if tipo == 'tabla':
            frags.append(tabla(*dato))
        elif tipo == 'figura':
            frags.append(figura(dato[0], dato[1], dato[2]))
        elif tipo == 'espacio':
            frags.append(espacio())
        else:
            frags.append(CONSTRUCTOR[tipo](dato))
        # una linea de aire despues de la ultima vineta de cada lista
    return frags, todos, origen


# ----------------------------------------------------------------- montaje
def main():
    if not os.path.exists(BASE):
        raise SystemExit('falta base.docx en %s' % AQUI)
    if os.path.isdir(UNP):
        shutil.rmtree(UNP)
    with zipfile.ZipFile(BASE) as z:
        z.extractall(UNP)
        nombres = z.namelist()

    frags, bloques, origen = contenido()

    tree = ET.parse(DOC)
    body = tree.getroot().find('w:body', NS)
    kids = list(body)
    sectPr = kids[-1]
    for el in kids[PORTADA:-1]:
        body.remove(el)

    nuevos = [el for frag in frags for el in xml(frag)]
    idx = list(body).index(sectPr)
    for n, el in enumerate(nuevos):
        body.insert(idx + n, el)
    tree.write(DOC, xml_declaration=True, encoding='UTF-8', method='xml')

    if os.path.exists(SALIDA):
        os.remove(SALIDA)
    with zipfile.ZipFile(SALIDA, 'w', zipfile.ZIP_DEFLATED) as z:
        for n in nombres:                       # mismo orden que el original
            z.write(os.path.join(UNP, n), n)
        ya = set(nombres)
        for raiz, _, ficheros in os.walk(UNP):
            for f in ficheros:
                ruta = os.path.join(raiz, f)
                rel = os.path.relpath(ruta, UNP).replace(os.sep, '/')
                if rel not in ya:
                    z.write(ruta, rel)
    shutil.rmtree(UNP)

    cuenta = {}
    for t, _ in bloques:
        cuenta[t] = cuenta.get(t, 0) + 1
    print('capitulos: %s' % ', '.join(capitulos()))
    print('bloques:   %s' % ', '.join('%s=%d' % kv for kv in sorted(cuenta.items())))
    for nombre, de in sorted(origen.items()):
        print('figura:    %-14s <- %s' % (nombre, de))
    print('escrito:   %s (%.1f MB)' % (os.path.basename(SALIDA),
                                       os.path.getsize(SALIDA) / 1e6))


if __name__ == '__main__':
    main()
