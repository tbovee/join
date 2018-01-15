#! /usr/bin/env python

# project as part of my learning python, restricted to the built-ins
<<<<<<< HEAD
# Version 20180114.2106
=======
# Version 20180114.1930
>>>>>>> parent of cb71295... join.py
# Next step: In joinfiles(), F3.write won't convert a list[item] with mixed strings and 
# integers into a string for writing to disk. 
# Converted importfiles(), importfile(), procline(),joinfiles()
# But the importfiles tree parameters are wrong, especially tbl.

'''
ERR DISCUSSION: Solutions to list conversion error:

Fix 1: Produce pointer lists to specific keys in bigtable and smalltable, 
keeping the tables as strings from the original files.

Fix 2: Do poiners, as in Fix 1, but only for smalltable, which carries the
largest search overhead

Fix 3: Don't use pointers. Instead, split the lines of bigtable and smalltable
each time the key is needed for a line. This carries the biggest overhead in
machine time, I suspect.

I'm leaning toward Fix 1 as the most efficient. This would require turning
procline into mechanism for creating bigptr and smallptr, each structured as
a list of lists, with each item having two fields: 
	[ptr to the current line number][data in the key positon of that file]
		

'''



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
table1 = []
table2 = []
key1 = 0 		# int points to the field containing the first key: default first field
key2 = 0		# int points to the field containing the second key: default first field
sep1 = ","		# char sets the field separator character in file1 to default comma
sep2 = ","		# char sets the field separator character in file2 to default comma
names1 = False	# bool if true, designates the first line of file1 to be fieldnames
names2 = False	# bool if true, designates the first line of file2 to be fieldnames
ptrs1 = []		# list holds the key data and record pointers from file 1
ptrs2 = []		# list holds the key data and record pointers from file 1
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

def procline(s,ptr,tbl,key,sep):
# Splits s into fields and inserts into appropriate lists
	s = s.rstrip()
	if len(s) > 0:
		curr = s.split(sep)
		key = curr[key]
		if key < len(curr):
			tbl.append(s)
			ptrs1.append(curr[key],ptr)
			s = ""
# END procline


def importfile(fileobj,ptrs,key,sep,names):
# Reads file from disk and passes each line to procfile()
	ptr = -1
	for line in fileobj :
		ptr = ptr + 1
		if ptr == 0:
			if names == False:
				procline(line,ptr,tbl,key,sep)
			#END if names....
		else:
			procline(line,ptr,tbl,key,sep)
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
	global bigptrs
	global bigkey
	global smallptrs
	global smallkey
	global count1
	global count2
		
	F1 = open(file1, 'r')
	count1 = importfile(F1,ptrs1,key1,sep1,names1)
	F1.close()
	F2 = open(file2, 'r')	
	count2 = importfile(F2,ptrs2,key2,sep2,names2)
	F2.close()
	if count1 > count2:
		bigtable = file1
		bigptrs = ptrs1
		bigkey = key1
		bigsep = sep1
		smalltable = table2
		smallptrs = ptrs2
		smallkey = key2
	else:
		bigtable = table2
		bigptrs = ptrs2
		bigkey = key2
		bigsep = sep2
		smalltable = table1
		smallptrs = ptrs2
		smallkey = key1
# END importfiles

def joinfiles():
	global F3
	global outfile
	global bigsep
	bigptr = -1
	smallptr = -1
	F3 = open(outfile, 'w')
	F3.close()
	F3 = open(outfile, "a")
	bigend = len(bigptrs) - 1
	smallend = len(smallptrs) -1
	if DEBUG == 1:
		print "len(bigptrs)=",len(bigptrs)
	outstr = ""
	if DEBUG == 1:
		print "bigptr=", str(bigptr)," smallptr=",str(smallptr), " bigend=",bigend
	while bigptr in range(-1,bigend):
		bigptr = bigptr + 1
		smallptr = -1
		while smallptr in range(-1,smallend):
			smallptr=smallptr + 1
			
			if DEBUG == 1:
				print str(smallptr)," "
			
			if smallptrs[smallptr][0] == bigtrs[bigptr][0]:
				if bigptrs[bigptr][-1] <> bigsep:
					bigtable[bigptr] = bigtable[bigptr],bigsep
				outstr = bigtable[bigptr],smalltable[smallptr]
				if DEBUG == 1:
					print "Outstr = ",outstr

				F3.write(outstr)
			
				outstr = ""
				break
	if DEBUG == 1:
		F3.write("The last word")
		
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