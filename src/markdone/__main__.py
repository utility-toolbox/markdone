# -*- coding=utf-8 -*-
r"""

"""
import argparse as ap
from . import __version__, markdone


parser = ap.ArgumentParser(prog='markdone', formatter_class=ap.ArgumentDefaultsHelpFormatter)
parser.add_argument('-v', '--version', action='version', version=__version__)


def main(argv=None):
    args = vars(parser.parse_args(argv))
    markdone(**args)


if __name__ == '__main__':
    main()
