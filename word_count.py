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

print(args) #returns Namespace, which indicates type of variable
print(args.data_file) #make sure it's reading in the data like it should


#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
