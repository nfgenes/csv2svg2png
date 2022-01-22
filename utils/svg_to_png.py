# svglib https://github.com/deeplook/svglib/blob/master/svglib/svglib.py

# svg2rlg function signature: svg2rlg(path, resolve_entities=False, **kwargs)
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

def generatePNG(file_path, name):
    drawing = svg2rlg(file_path)
    renderPM.drawToFile(drawing, f'output/{name}.png', fmt='PNG')

