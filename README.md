# PHiGGS

## (P)ython (Hi)erarchical (G)raph (G)enerating (S)ystem

PHiGGS is the result of my frustration with the inability of existing graphing tools to generate family tree diagrams that support (1) multiple parents, (2) spouse-to-spouse connections, and (3) hierarchical structures. After two weeks of exhaustive searching, I couldn't find anything that met my needs, so here I am writing a Python 3 framework for generating directed acyclic graphs (DAGs) that look like hierarchical tree diagrams.

### Dependencies

- Python (>= v3.4)
- Graphviz (>= v2.4)

### Installation

TBD

### Usage

``` bash
    usage: phiggs [-h] -i INPUT -e EXT [-s STYLE]

        PHiGGS: (P)ython (Hi)erarchical (G)raph (G)enerating (S)ystem
        Copyright (c) 2018, Benjamin S. Meyers <admin@lionlogic.org>

    Information:
        -h, --help                  show this help message and exit

    Required:
        -i INPUT, --input INPUT     input file containing graph data
        -e EXT, --extension EXT     output file format

    Optional:
        -s STYLE, --style STYLE     custom stylesheet for graph elements

```

### Customization

TBD

### Contributing

TBD

### Contact

Benjamin S. Meyers < admin@lionlogic.org >

### License

[MIT](https://github.com/meyersbs/PHiGGS/blob/master/LICENSE.md)
