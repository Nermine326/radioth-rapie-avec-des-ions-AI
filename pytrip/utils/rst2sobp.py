
"""
This script converts a raster scan file in GSI format to a sobp.dat file which can be used by FLUKA or SHIELD-HIT12A
to simulate the beam using Monte Carlo methods.
"""
import sys
import logging
import argparse
import pytrip as pt


def main(args=None):
    """ Main function of the rst2sobp script.
    """
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("rst_file", help="path to .rst input file in TRiP98 format", type=str)
    parser.add_argument("sobp_file", help="path to the SHIELD-HIT12A/FLUKA sobp.dat output file", type=str)
    parser.add_argument("-v", "--verbosity", action='count', help="increase output verbosity", default=0)
    parser.add_argument('-V', '--version', action='version', version=pt.__version__)
    args = parser.parse_args(args)

    rst = pt.Rst()
    rst.read(args.rst_file)

    with open(args.sobp_file, 'w') as fout:
        fout.writelines("*ENERGY(GEV) X(CM)  Y(CM)     FWHM(cm)  WEIGHT\n")
        for subm in rst.machines:
            for xpos, ypos, part in subm.raster_points:
                fout.writelines("{:<10.6f}{:<10.2f}{:<10.2f}{:<10.2f}{:<10.4e}\n".format(
                    subm.energy / 1000.0, xpos / 10.0, ypos / 10.0, subm.focus / 10.0, part))
    return 0


if __name__ == '__main__':
    logging.basicConfig()
    sys.exit(main(sys.argv[1:]))
