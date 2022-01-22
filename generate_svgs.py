import csv
import inspect

genesFile = 'genes.csv'

with open(genesFile, 'r') as genesData:
    dataStream = csv.DictReader(genesData, delimiter=',')
    for row in dataStream:
        print(row['Gene symbol'])
        geneSymbol = row['Gene symbol']
        geneName = row['Gene name']
        geneLength = row['Gene length']
        geneLocalization = row['Gene localisation']
        geneLocalizationSplit = geneLocalization.split(":")

        svgText = f"""
            <?xml version="1.0" encoding="UTF-8"?>
            <svg width="350px" height="250px" viewbox="0 0 350 250" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
            <style>
                .geneSymbol {{ font-size: 45px; font-weight: bold; fill: black; }}
                .geneName {{ font-size: 20px; }}
                .geneLength {{ font-size: 20px; }}
                .geneLocalization {{ font-size: 20px; fill: blue; }}
            </style>
            <text x="20" y="65" class="geneSymbol">{geneSymbol}</text>
            <text x="20" y="105" class="geneName">{geneName}</text>
            <text x="20" y="145" class="geneLength">{geneLength} Bases</text>
            <text x="20" y="185" class="geneLocalization">{geneLocalizationSplit[0]}: </text>
            <text x="20" y="225" class="geneLocalization">{geneLocalizationSplit[1]}</text>
            </svg>
        """

        svgTextCleaned = inspect.cleandoc(svgText)
        svgTextNoLines = svgTextCleaned.replace('/n', "")

        svgfile = open(f'input/{geneSymbol}.svg', 'w')
        svgfile.write(svgTextNoLines)