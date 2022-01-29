# NFgenes 🧬⛓ - csv2svg2png
Python scripts to convert NFgene source data from csv to SVG and PNG

This library is a simple conversion utility to take the source data compiled for the NFgenes genesis mint and create an SVG and PNG file for each.

### generate_svgs.py

```python
# Will read the file 'genes.csv' in the root dir and generate an
# svg file for each row and store them in the './input' dir.
$ python3 generate_svgs.py
```

### generate_pngs.py

```python
# Will iterate through each file in the '/input' dir and
# generate a png file for each.
$ python3 generate_pngs.py
```

Learn more about the [NFgenes 🧬⛓ project](https://github.com/nfgenes/overview#nfgenes-nonfungible-genes-overview)
