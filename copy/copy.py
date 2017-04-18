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
        elif len(self.list_argv) >= 1 and (''.join(self.list_argv[1:])):
            self.argument_list = (''.join(self.list_argv[1:]))
            Model().copy_file()
        elif len(self.list_argv) >= 1:
            View().print_with_one_argument_provided()

class Model(object):

    def copy_file(self):
        self.destination = open("destination.txt", 'a+')
        self.read_lines_from_destination = self.destination.readlines()
        self.source = open("source.txt", 'r')
        self.read_lines_from_file = self.source.readlines()
        for lines in self.read_lines_from_file:
            self.destination.write("\n" + lines)
        self.source.close()
        self.destination.close()
        
class View(object):

    def print_usage(self):
        print("copy [source] [destination]")

    def print_with_one_argument_provided(self):
        print("No destination provided")

controller = Controller()
model = Model()
view = View()
