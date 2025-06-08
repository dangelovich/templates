#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Template for basic python scripting purposes
"""

import logging
import pprint
import sys
import argparse
import time
import yaml


def setuplogging(arguments):
    """ Set up logging for the script """
    logging.getLogger("requests").setLevel(logging.ERROR)
    FORMAT="%(levelname)s:%(funcName)s:%(message)s"
    LEVEL=logging.ERROR
    if arguments.debug:
        LEVEL=logging.DEBUG
    if arguments.verbose:
        LEVEL=logging.INFO
    logging.basicConfig(level=LEVEL, format=FORMAT)


def process_arguments(argument_list, name):
    """ Process arguments passed in """
    parser = argparse.ArgumentParser(description=name)

    parser.add_argument('-v', "--verbose",
                         action="store_true",
                         help="Enable verbose mode",
                         default=False)
    parser.add_argument('-d', "--debug",
                         action="store_true",
                         help="Enable debug mode",
                         default=False)
    parser.add_argument('-c', '--config',
                        action="store",
                        dest="config",
                        type=str,
                        help="Config file",
                        required=False,
                        default="config.yaml")

    return parser.parse_args(argument_list)


def getconfig(configfile):
    """ Open the supplied configuration file and import its contents as yaml """
    try:
        with open(configfile, "r") as ymlfile:
            config = yaml.load(ymlfile, Loader=yaml.SafeLoader)
            logging.debug("Config file contents:\n%s", pprint.pformat(config))
            logging.info("Config file loaded successfully")
        ymlfile.close()
    except IOError as configioexception:
        logging.error("Error reading from config file: %s.\n Error: %s",
                        configfile, configioexception)
        sys.exit()
    return config


def main():
    """ Main function """
    # Update the variable below to the app name
    script_name = "Template"
    args = process_arguments(sys.argv[1:], script_name)

    setuplogging(args)

    logging.debug("Starting %s", script_name)
    script_start_time = float(time.time_ns())

    config = getconfig(args.config)

    # App starts here
    print("Hello, world!")

    logging.debug("Finished in %f seconds", ((time.time_ns() - script_start_time)/1000000000))


if __name__ == '__main__':
    main()
