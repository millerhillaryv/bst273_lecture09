#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser( description="" )


parser.add_argument(
	"data_file",
	help = "path to the file we want to read",
)



#-------------------------------------------------------------------------------
# Are there other arguments we need?
#-------------------------------------------------------------------------------

args = parser.parse_args( )

print("args =", args) #returns Namespace, which indicates type of variable
print("args data file =", args.data_file) #make sure it's reading in the data like it should

#fh = file handle
fh = open(args.data_file)
print("the file handle is", fh)


#count variables - set = 0 
lines = 0
words = 0
chars = 0
#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
