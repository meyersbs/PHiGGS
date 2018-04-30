#!/usr/bin/env python3

__author__ = "Benjamin S. Meyers"
__title__ = "PHiGGS: (P)ython (Hi)erarchical (G)raph (G)enerating (S)ystem"
__copyright__ = "Copyright (c) 2018, Benjamin S. Meyers"
__credits__ = ["Benjamin S. Meyers"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Benjamin S. Meyers"
__email__ = "admin@lionlogic.org"
__status__ = "development"

__help__ = "\t" + __title__ + "\n\t" + __copyright__ + " <" + __email__ + ">"

import argparse
from argparse import RawTextHelpFormatter

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=RawTextHelpFormatter, description=__help__
    )

    parser._optionals.title = "Information"

    req_group = parser.add_argument_group("Required")
    req_group.add_argument(
        "-i", "--input", dest="input", metavar="INPUT", default=None,
        required=True, help="input file containing graph data"
    )
    req_group.add_argument(
        "-e", "--extension", dest="ext", metavar="EXT", default="svg",
        required=True, help="output file format", choices=["svg"]
    )

    opt_group = parser.add_argument_group("Optional")
    opt_group.add_argument(
        "-s", "--style", dest="style", metavar="STYLE", default="default",
        required=False, help="custom stylesheet for graph elements"
    )

    parser.parse_args()
