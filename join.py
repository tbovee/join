#! /usr/bin/env python

# project as part of my learning python, restricted to the built-ins
# Version 20180113.1108A
# ERR STATUS: filename param unpassed to importfile()

'''
PURPOSE
:
Program joins two records from files together, each having a common key.
END PURPOSE

INVOKE:

join.py input-filename1 input-filename2 -output-filename [-type] [value] ...

The names of the files containing the records to be joined require no -type and must be
in the first three positions of the commandline parameters.
The first filename entered is input for table1 in the code, 
and the second entered is input for table2. The third entered is the output file.

Other parameters take a -type (such as -sep to specify the character that
separates fields in a record), and then in the next positon, that parameter for the
specified -type.

The types, meanings and defaults are:

-k1, -k2 points to the column containing the key field, where zero is
	the leftmost column. Default: 0
-s1, -s2 points to the character used to separat fields. The character
	must be surrounded by quote marks on the commandline. Default: ","
-n1, -n2 informs that the first column of the file contains the names
	of the fields and sets a flag in code to TRUE. 
	It requires no value. Default (i.e., the -n1 or -n2 flag is absent
	from the commandline): FALSE
END INVOKE

'''

# Command line arguments

# Global names
file1 = ""  	# str points to the first input file
file2 = ""  	# str points to the second input file
outfile = "" 	# str points to the output product
key1 = 0 		# int points to the field containing the first key: default first field
key2 = 0		# int points to the field containing the second key: default first field
sep1 = ","		# char sets the field seprator character in file1 to default comma
sep2 = ","		# char sets the field seprator character in file2 to default comma
names1 = False	# bool if true, designates the first line of file1 to be fieldnames
names2 = False	# bool if true, designates the first line of file2 to be fieldnames
table1 = []		# list holds the parsed data from file1
table2 = []		# list holds the parsed data from file2
bigtable = []		# list holds the data with the greater number of records
smalltable = []		# list holds the data with the smaller number of records

# END Global names

# Import modules
import sys
# import pandas as pd # For revision after completion, maybe
# END Import modules


def arguments():
# Get arguments
	n = len(sys.argv)-1
	if n < 3:
		print "Usage: join.py input-filename1 input-filename2 -output-filename [-type] [value] ..."
		return -1
	else:	
		file1 = sys.argv[1]
		file2 = sys.argv[2]
		outfile = sys.argv[3]
		for i in range(4,n):
			if sys.argv[i] == '-kl':
				key1 = sys.argv[i+1]
			elif sys.argv[i] == '-k2':
				key2 = sys.argv[i+1]
			elif sys.argv[i] == '-s1':
				sep1 = sys.argv[i+1]
			elif sys.argv[i] == '-s2':
				sep2 = sys.argv[i+1]
			elif sys.argv[i] == '-n1':
				names1 = TRUE
			elif sys.argv[i] == '-n2':
				names2 = TRUE
#END Get arguments()

def procline(s,table,key,sep):
# Splits s into fields and inserts into appropriate lists
  	curr = s.split(sep)
  	k = len(curr)
	if key < k:
		table.append(curr)
# END procline


def importfile(filename,table,key,sep,names):
# Reads file from disk and passes each line to procfile()
	pointer = 0
	print "Filename:"
	print filename
	sys.exit()
	F = open(filename, 'r')
	for line in F :
		if pointer == 1:
			if names == FALSE:
				procline(line,table,key,sep)
		else:
			procline(line,table,key,sep)
	return len(table)
# END importfile

def importfiles():
# Imports the input files in turn, assesses the size of each, and assigns
# the larger to the big... series of lists and the smaller to the small...
# series of lists
	global file1
	global file2
	global bigtable
	global bigkey
	global smalltable
	global smallkey
	global table1
	global table2
	count1 = importfile(file1,table1,key1,sep1,names1)
	count2 = importfile(file2,table2,key2,sep2,names2)
	if count1 > count2:
		bigtable = table1
		bigkey = key1
		smalltable = table2
		smallkey = key2
	else:
		bigtable = table2
		bigkey = key2
		smalltable = table1
		smallkey = key1
	'''
	Truncating import files and tables to reclaim memory	
	'''
	file1 = ""
	file2 = ""
	table1 = []
	table2 = []
# END importfiles

def main() :
	if arguments() == -1:
		return
	else:
		importfiles()
		# Test output
		print "Bigkey"
		print bigkey
		print "Smallkey"
		print smallkey
		print "Bigtable"
		print bigtable
		print "Smalltable"
		print smalltable
	# END Test output
	return
#End main

# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--