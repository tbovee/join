#! /usr/bin/env python

# project as part of my learning python, restricted to the built-ins
# Version 20180109.1140P

'''
Program joins two records from files together, each having a common key.

Invoke:

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

'''

'''
OVERVIEW:

Read the command line arguments.

Load file1 and file 2 into separate lists.
	For each file,
	split each line and extract the key data; increment the tablecount to create the
	ptr data; add each their ptr lists.
	While loading extact the key field data and the line number into a ptr list
	Ptr list structure: keydata, pointer, keydata, pointer...
		where the pointer is associated with the preceding keydata.

Joining the files

After the table lists are loaded, compare tablecount1 and tablecount2. 
If tablecount1 is larger than tablecount2, then assign 
tablecount1 to smalltable; otherwise, assign it to bigtable. Assign
the unassigned numbered table to the yet unassigned bigtable or smalltable.

Assign the associated pointer lists in the same way, ptr1 and ptr2 to bigptr and 
smallptr.

Each table has a separate function.

The ptr list for the largest, bigtable, is read one line at a time. 
For each key it contains, it loops through the pointers of the 
other table, smalltable, until it finds a matching key.
When a matching key is found, the two lines are combined and written to
the output file, outfile.

#END 

'''

# Command line arguments

# Global names
file1 = ""
file2 = ""
outfile = ""
key1 = 0
key2 = 0
sep1 = ","
sep2 = ","
names1 = False
names2 = False

tablecount1 = 0
tablecount2 = 0

bigtable = ""
smalltable = ""
bigptr = ""
smallptr = ""

# Import modules
import sys
# import pandas as pd # For revision after completion, maybe

n = len(sys.argv)-1
# Error checking here if n < 2
file1 = sys.argv[0]
file2 = sys.argv[1]
outfile = sys.argv[2]
for i in range(2,n):
	elif sys.argv[i] == '-kl':
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
	else
		help()


def importfile(filename,delim,key,k) :
  F = open (filename, 'r')
  first = 0
  for line in F :
	  	# Split into fields
  	curr = line.split(delim)
	  	# Save the number of fields
  	if first == 0:
  		k = len(curr)
  		first = 1
  		# Test lioness
  	# Add curr to 
  	print curr
  		# End Test
# End importfile




def main() :

	  # Test run

	print "Print args"
	print fileleft
	print tableright
	print keyleft
	print keyright
	print delimleft
 	print delimright
 	print colnames


	importfile(fileleft,",",1,kleft)
	importfile(fileright,",",3,kright)
	
	return
		# End Test  
#End main

# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--