from utils import svg_to_png
import os

directory = 'input'

for filename in os.listdir(directory):
    filePath = f'input/{filename}'
    print(filePath)
    svg_to_png.generatePNG(filePath, os.path.splitext(filename)[0])