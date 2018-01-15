#! /usr/bin/env python

# project as part of my learning python, restricted to the built-ins
# Version 20180115.1231

# Current issues:
# Concatenation of string joins to produce joined string.
# They are being treated as tuples rather than strings.
# The source of the strings is table[n][1]

# It appears impossible to pluck a string from a field in a list
# and find it intact in the form in which was entered.

# Solution: abandon table1 and table2. 
# In procline(), create lists (ptrs1, ptrs2) for file1 and file2 that have two fields:
# 	[data[key],[fileN->ptr], where ptr = line number
# In joinfiles(), 


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

DEBUG = 1
# Command line arguments

# Global names
file1 = ""  	# str points to the first input file
file2 = ""  	# str points to the second input file
outfile = "" 	# str points to the output product
table1 = []		# [str][int] where str is data[key] and int is the line# in file1
table2 = []		# [str][int] where str is data[key] and int is the line# in file2
key1 = 0 		# int points to the field containing the first key: default first field
key2 = 0		# int points to the field containing the second key: default first field
sep1 = ","		# char sets the field separator character in file1 to default comma
sep2 = ","		# char sets the field separator character in file2 to default comma
names1 = False	# bool if true, designates the first line of file1 to be fieldnames
names2 = False	# bool if true, designates the first line of file2 to be fieldnames
bigtable = []		# list holds the csv lines for the file with the greater number of records
smalltable = []		# list holds the csv lines for the file with the smaller number of records
bigsep = ","		# used in joinfiles()

count1 = 0
count2 = 0

# END Global names

# Import modules
import sys
# import pandas as pd # For revision after completion, maybe
# END Import modules


# Get arguments
n = len(sys.argv)-1
if n < 3:
	print "Usage: join.py input-filename1 input-filename2 -output-filename [-type] [value] ..."
	sys.exit()
else:	
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	outfile = sys.argv[3]
	for i in range(4,n):
		if sys.argv[i] == '-k1':
			key1 = int(sys.argv[i+1])
		elif sys.argv[i] == '-k2':
			key2 = int(sys.argv[i+1])
		elif sys.argv[i] == '-s1':
			sep1 = sys.argv[i+1]
		elif sys.argv[i] == '-s2':
			sep2 = sys.argv[i+1]
		elif sys.argv[i] == '-n1':
			names1 = TRUE
		elif sys.argv[i] == '-n2':
			names2 = TRUE
#END get arguments

def procline(s,tbl,key,sep,ptr):
# Splits s into fields and inserts key field and full string into appropriate lists
	s = s.rstrip()
	if len(s) > 0:
		curr = s.split(sep)
		if key < len(curr):
			rec = [curr[key],ptr]
			tbl.append(rec)
			s = ""
# END procline


def importfile(fileobj,tbl,key,sep,names):
# Reads file from disk and passes each line to procfile()
	ptr = -1
	for line in fileobj :
		ptr = ptr + 1
		if ptr == 0:
			if names == False:
				procline(line,tbl,key,sep,ptr)
			#END if names....
		else:
			procline(line,tbl,key,sep,ptr)
		#END if ptr...
	return len(tbl)
# END importfile

def importfiles():
# Imports the input files in turn, assesses the size of each, and assigns
# the larger to the big... series of lists and the smaller to the small...
# series of lists
	global F1
	global F2
	global file1
	global file2
	global table1
	global table2
	global bigtable
	global smalltable
	global bigkey
	global smallkey
	global count1
	global count2
	
	F1 = open(file1, 'r')
	count1 = importfile(F1,table1,key1,sep1,names1)
	F1.close()
	F2 = open(file2, 'r')	
	count2 = importfile(F2,table2,key2,sep2,names2)
	F2.close()
	if count1 > count2:
		bigtable = file1
		bigfile = file1
		bigkey = key1
		bigsep = sep1
		smalltable = table2
		smallfile = file2
		smallkey = key2
		
	else:
		bigtable = table2
		bigfile = file2
		bigkey = key2
		bigsep = sep2
		smalltable = table1
		smallfile = file1
		smallkey = key1
# END importfiles

def getline(filename,ptr)
	i = 0
	F4 = open(filename, "r")
	for line in F4:
		if i == ptr:
			return line
			break
		else:
			i = i + 1
# END getline()

def joinfiles():
	global F3
	global outfile
	global bigtable
	global smalltable
	global bigsep
	bigptr = -1
	smallptr = -1
	if DEBUG == 1:
		print "In joinfiles():"
	F3 = open(outfile, 'w')
	F3.close()
	F3 = open(outfile, "a")
	bigend = len(bigtable) - 1
	smallend = len(smalltable) - 1
	
	while bigptr in range(-1,bigend):
		bigptr = bigptr + 1
		smallptr = -1
		while smallptr in range(-1,smallend):
			smallptr=smallptr + 1
			
			if smalltable[smallptr][0] == bigtable[bigptr][0]:
				linebig = getline(bigfile,bigptr)
				linesmall = getline(smallfile,smallptr)
				if linebig[-1] <> bigsep:
					linebig = linebig + bigsep
				if linesmall[-1] <> smallsep:
					linesmall = linesmal + smallsep
				F3.write(linebig + linesmall)
				F3.write(str(smalltable[smallptr][1]))
				
				if DEBUG == 1:
					print linebig + linesmall

				break
	if DEBUG == 1:
		F3.write("\nThe last word")
		
	F3.close()
#end joinfiles()
				
def main() :
	importfiles()
	joinfiles()
	return
#End main

# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--