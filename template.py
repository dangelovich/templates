#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Template for basic python scripting purposes
"""

import logging
import yaml
import pprint

def setuplogging(arguments):
    """ Set up logging for the script """
    logging.getLogger("requests").setLevel(logging.ERROR)
    if arguments.debug:
        logging.basicConfig(level=logging.DEBUG)
    if arguments.verbose:
        logging.basicConfig(level=logging.INFO)


def doArgs(argList, name):
    """ Process arguments passed in """
    parser = argparse.ArgumentParser(description=name)

    parser.add_argument('-v', "--verbose", action="store_true", help="Enable verbose mode", default=False)
    parser.add_argument('-d', "--debug", action="store_true", help="Enable debug mode", default=False)
    parser.add_argument('-c', '--config', action="store", dest="config", type=str, help="Input file name", required=True)
    parser.add_argument('--output', action="store", dest="outputFn", type=str, help="Output file name", required=True)

    return parser.parse_args(argList)


def main():
    progName = "Template"
    args = doArgs(sys.argv[1:], progName)

    verbose = args.verbose
    inputFn = args.inputFn
    outputFn = args.outputFn

    print "Starting %s" % (progName)
    startTime = float(time.time())

    if not os.path.isfile(inputFn):
        print "Input doesn't exist, exiting"
        return

    outputBase = os.path.dirname(outputFn)
    if outputBase!='' and not os.path.exists(outputBase):
        print "Output directory doesn't exist, making output dirs: %s" % (outputBase)
        os.makedirs(outputBase)


    print "Finished in %0.4f seconds" % (time.time() - startTime)
    return


if __name__ == '__main__':
    #sys.argv = ["programName.py","--input","test.txt","--output","tmp/test.txt"]
    main()
