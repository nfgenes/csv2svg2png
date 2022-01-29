# NFgenes (NonFungible Genes) Overview

NFgenes is a decentralized science (DeSci) project aiming to bring data and collaboration for human genome research to the blockchain. Share knowledge, create value, build a community and teach science.

- [Roadmap](https://github.com/nfgenes/overview#roadmap)
- [NFgene List and Genesis Collection](https://github.com/nfgenes/nfgenes_list#nfgenes-nonfungible-genes-overview)
    - [NFgenes List](https://github.com/nfgenes/nfgenes_list/tree/main/data#nfgenes-list)
        - [Demo Proof of Concept: Storing NFgenes List on IPFS](https://nfgeneslist.onrender.com/)
        - [Repository](https://github.com/nfgenes/front_end_nfgenes_list#nfgenes-nonfungible-genes-overview)
    - [Genesis NFT Collection](https://github.com/nfgenes/nfgenes_contract)
- [Methodology for Compiling original list of NFgenes](https://github.com/nfgenes/compile_genesis_gene_list)
- Utilities
    - [Merkle Tree generator](https://github.com/nfgenes/merkletree_generator)
    - [Python scripts to convert NFgene source data from csv to SVG and PNG](https://github.com/nfgenes/csv2svg2png#csv2svg2png)

------------

# csv2svg2png
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