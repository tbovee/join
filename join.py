#! /usr/bin/env python

# project as part of my learning python, restricted to the built-ins
# Version 20180113.1020A
# ERR STATUS: var table is local and global in import routines
# TODO: Drop the pointers, use multidimensional lists

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
pointers1 = ""
pointers2 = ""
pointer1 = 0
pointer2 = 0

bigtable = ""		# list holds the data with the greater number of records
smalltable = ""		# list holds the data with the smaller number of records
bigpointers = ""	# list holds the key data and pointer for each line in bigtable
smallpointers = ""	# list holds the key data and pointer for each line in smalltable.
bigpointer = ""		# int points to current record in bigable
smallpointer = ""	# int points to current record in smalltable

# END Global names

# Import modules
import sys
# import pandas as pd # For revision after completion, maybe
# END Import modules


def arguments():
# Get arguments
	n = len(sys.argv)-1
	if n < 2:
		print "Usage: join.py input-filename1 input-filename2 -output-filename [-type] [value] ..."
		return -1
	else:	
		file1 = sys.argv[0]
		file2 = sys.argv[1]
		outfile = sys.argv[2]
		for i in range(2,n):
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

def procline(s,sep,key,table,pointers,pointer):
# Splits s into fields and inserts into appropriate lists
	'''
	Is the var tablecount needed here?
	'''
  	curr = s.split(sep)
  	k = len(curr)
	if key < k:
		table.append(curr)
		pointers.append(curr[key])
		pointers.append(pointer)
# END procline


def importfile(sep,key,table,pointers,pointer,file,names):
# Reads file from disk and passes each line to procfile()
	global table

	'''
	Q: Would it be more efficient to read the entire file into a list and then get the size
	from the list rather than doing a count? Probably yes.
	'''
	pointer = 0
	F = open(file, 'r')
	for line in F :
		if pointer == 1:
			if names == FALSE:
				procline(line,sep,key,table,pointers)  
			else:
				procline(line,sep,key,table,pointers)  
	return len(table)
# END importfile

def importfiles():
# Imports the input files in turn, assesses the size of each, and assigns
# the larger to the big... series of lists and the smaller to the small...
# series of lists
	global bigfile
	global bigkey
	global smallfile
	global smallkey
	global pointers1
	global pointers2
	global pointer1
	global pointer2
	count1 = importfile(sep1,key1,pointers1,pointer1,file1,names1)
	count2 = importfile(sep2,key2,pointers2,pointer2,file2,names2)
	if count1 > count2:
		bigfile = file1
		bigkey = key1
		smallfile = file2
		smallkey = key2
	else:
		bigfile = file2
		bigkey = key2
		smallfile = file1
		smallkey = key1
	'''
	Truncating import files to reclaim memory	
	'''
	file1 = ""
	file2 = ""
	pointers1 = ""
	pointers2 = ""
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