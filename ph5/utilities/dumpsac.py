#!/usr/bin/env pnpython3

#
#   Translate and dump a binary SAC file to stdout
#
#   December 2013, Steve Azevedo
#

import sys
import logging
from ph5.core import sacreader

PROG_VERSION = '2018.268'
LOGGER = logging.getLogger(__name__)


def get_args():
    global INFILE, PRINT, ENDIAN

    from optparse import OptionParser
    oparser = OptionParser()

    oparser.usage = "Version: {0} Usage: dumpsac [options]".format(
        PROG_VERSION)

    oparser.add_option("-f", action="store", dest="infile", type="string")

    oparser.add_option("-p", action="store_true",
                       dest="print_true", default=False)

    options, args = oparser.parse_args()

    if options.infile is not None:
        INFILE = options.infile
    else:
        LOGGER.error("No infile given.")
        sys.exit()

    PRINT = options.print_true


def print_it(header):
    try:
        keys = sorted(header.keys())
        for k in keys:
            print "{0:<12}\t{1:<12}".format(k, header[k])
    except AttributeError:
        for t in header:
            print t


def main():
    get_args()
    sr = sacreader.Reader(infile=INFILE)
    print "Endianness: {0}".format(sr.endianness)
    print "+------------+"
    print "|Float Header|"
    print "+------------+"
    print_it(sr.read_float_header())
    print "+--------------+"
    print "|Integer Header|"
    print "+--------------+"
    ret = sr.read_int_header()
    print_it(ret)
    print "+----------------+"
    print "|Character Header|"
    print "+----------------+"
    print_it(sr.read_char_header())
    if PRINT:
        print "+-----+"
        print "|Trace|"
        print "+-----+"
        print_it(sr.read_trace(ret['npts']))


if __name__ == '__main__':
    main()
