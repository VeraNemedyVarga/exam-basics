# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination

import sys

class Controller(object):

    def __init__(self):
        self.list_argv = []
        self.arg_reader()
        self.controller()

    def arg_reader(self):
        if len(sys.argv) <= 1:
            self.list_argv = []
        else:
            self.list_argv = sys.argv[1:]

    def controller(self):
        if len(self.list_argv) == 0:
            View().print_usage()


class View(object):

    def print_usage(self):
        print("copy [source] [destination]")

controller = Controller()
view = View()
