#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""docx -> markdown. El camino inverso de build.py.

Lee un .docx hecho sobre la plantilla de TX Intelligence y saca su contenido
como Markdown, un archivo por capitulo. Clasifica cada bloque por los mismos
marcadores que build.py escribe:

    Heading1  -> #      Heading2 -> ##     Heading3 -> ###
    Subtitle  -> ####   numPr    -> -      pBdr/left -> >
    w:drawing -> ![leyenda](figura.png "ancho en pulgadas")
    w:tbl     -> tabla markdown, con los anchos en un comentario

La PORTADA no se extrae: es parte de la plantilla y build.py la conserva tal
cual del docx base. Aqui solo sale el cuerpo.

Se usa una vez para sembrar los .md desde el docx que manda. A partir de ahi
el Markdown es la fuente y build.py lo devuelve al docx.

    python extraer.py [ruta-al-docx]
"""
import io
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
WP = 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'
Q = lambda t: '{%s}%s' % (W, t)

AQUI = os.path.dirname(os.path.abspath(__file__))
DESTINO = os.path.dirname(AQUI)          # documento/
PORTADA = 18                             # elementos 0..17 del cuerpo


def texto_de(el):
    """Junta los runs. Marca **negrita** cuando la fuente es SemiBold o hay w:b."""
    partes = []
    for r in el.iter(Q('r')):
        t = ''.join(n.text or '' for n in r.iter(Q('t')))
        if not t:
            continue
        rpr = r.find(Q('rPr'))
        neg = False
        if rpr is not None:
            f = rpr.find(Q('rFonts'))
            if f is not None and 'SemiBold' in (f.get(Q('ascii')) or ''):
                neg = True
            b = rpr.find(Q('b'))
            if b is not None and b.get(Q('val')) not in ('0', 'false'):
                neg = True
        partes.append(('**%s**' % t) if neg else t)
    return re.sub(r'\*\*\*\*', '', ''.join(partes)).strip()


def clasificar(el):
    pr = el.find(Q('pPr'))
    if pr is None:
        return 'p'
    est = pr.find(Q('pStyle'))
    est = est.get(Q('val')) if est is not None else ''
    if est in ('Heading1', 'Heading2', 'Heading3', 'Subtitle'):
        return est
    if pr.find(Q('numPr')) is not None:
        return 'vineta'
    b = pr.find(Q('pBdr'))
    if b is not None and b.find(Q('left')) is not None:
        return 'cita'
    return 'p'


MARCA = {'Heading1': '# ', 'Heading2': '## ', 'Heading3': '### ',
         'Subtitle': '#### ', 'vineta': '- ', 'cita': '> ', 'p': ''}
SIN_NEGRITA = ('Heading1', 'Heading2', 'Heading3', 'cita')   # el estilo ya la lleva


def cuerpo(doc_xml):
    body = ET.fromstring(doc_xml).find(Q('body'))
    els = list(body)[PORTADA:]
    salida, fig = [], None

    for el in els:
        # ---------------------------------------------------------- tabla
        if el.tag == Q('tbl'):
            grid = el.find(Q('tblGrid'))
            anchos = ([int(g.get(Q('w'))) for g in grid if g.get(Q('w'))]
                      if grid is not None else [])
            filas = [[texto_de(tc) for tc in tr.findall(Q('tc'))]
                     for tr in el.findall(Q('tr'))]
            filas = [f for f in filas if any(c.strip() for c in f)]
            if not filas:
                continue
            n = len(filas[0])
            salida += ['<!-- anchos: %s -->' % ','.join(str(a) for a in anchos[:n]),
                       '| ' + ' | '.join(filas[0]) + ' |',
                       '|' + '---|' * n]
            salida += ['| ' + ' | '.join(f) + ' |' for f in filas[1:]]
            salida.append('')
            continue

        if el.tag != Q('p'):
            continue

        # --------------------------------------------------------- figura
        dib = el.find('.//' + Q('drawing'))
        if dib is not None:
            ext = dib.find('.//{%s}extent' % WP)
            ancho = int(ext.get('cx')) / 914400.0 if ext is not None else 5.6
            nombre = next((d.get('name') for d in dib.iter()
                           if d.tag.endswith('}docPr') and d.get('name')), 'figura.png')
            fig = (nombre, ancho)
            continue

        tipo = clasificar(el)
        txt = texto_de(el)

        # el parrafo que sigue al dibujo es su leyenda
        if fig is not None:
            if txt:
                salida += ['![%s](%s "%.2f")' % (txt, fig[0], fig[1]), '']
                fig = None
                continue
            fig = None

        if not txt:
            continue
        if tipo in SIN_NEGRITA:
            txt = txt.replace('**', '')
        # una linea en blanco al salir de una lista, para que no se pegue
        if tipo != 'vineta' and salida and salida[-1].startswith('- '):
            salida.append('')
        salida.append(MARCA[tipo] + txt)
        if tipo != 'vineta':
            salida.append('')

    return salida


def partir(lineas):
    """Corta por Heading1. Lo anterior al primero va a 00-portada."""
    caps, act = [], ('Portada', [])
    for l in lineas:
        if l.startswith('# '):
            if any(x.strip() for x in act[1]):
                caps.append(act)
            act = (l[2:].strip(), [l, ''])
        else:
            act[1].append(l)
    if any(x.strip() for x in act[1]):
        caps.append(act)
    return caps


ACENTOS = str.maketrans('áéíóúñÁÉÍÓÚÑ', 'aeiounAEIOUN')


def slug(titulo, n):
    t = titulo.translate(ACENTOS).lower()
    t = re.sub(r'^\**\s*\d+\.\s*', '', t)     # quita "1. " y asteriscos sueltos
    t = re.sub(r'[:,].*$', '', t)
    t = re.sub(r'[^a-z0-9]+', '-', t).strip('-')
    return '%02d-%s' % (n, t[:34] or 'seccion')


def main(ruta):
    z = zipfile.ZipFile(ruta)
    lineas = cuerpo(z.read('word/document.xml').decode('utf-8'))
    caps = partir(lineas)

    for viejo in os.listdir(DESTINO):
        if re.match(r'^\d\d-.*\.md$', viejo):
            os.remove(os.path.join(DESTINO, viejo))

    print('extraido de: %s' % os.path.basename(ruta))
    print('capitulos:   %d\n' % len(caps))
    for n, (titulo, ls) in enumerate(caps):
        nombre = slug(titulo, n) + '.md'
        txt = re.sub(r'\n{3,}', '\n\n', '\n'.join(ls).strip()) + '\n'
        io.open(os.path.join(DESTINO, nombre), 'w',
                encoding='utf-8', newline='\n').write(txt)
        print('   %-36s %4d lineas  %5d palabras'
              % (nombre, txt.count('\n'), len(txt.split())))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else
         os.path.join(AQUI, 'Metodologia-AI-DLC-v1.0.docx'))
