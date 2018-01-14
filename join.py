#! /usr/bin/env python

# project as part of my learning python, restricted to the built-ins
# Version 20180114.1512
# ERR STATUS: file2 not being processed downstream; the processed array
# isn't being appended to table2

'''
ERROR DISCUSSION failure of procline on file2.

The failure n procline comes at the key test, which is designed to eliminate keys 
that exceed the number of fields.

The test is: 
	k = len(curr) # where curr is the current raw line from the file
	if key < k:
		#process the line
In the case of file1, the key is zero and k is 5. 
The statement key < k is interpreted as True.

In the case of file2, the key is 2 and k is 8.
The statement key < k is interpreted as False.

I don't get it.

OUTPUT of the run:

sierra:join tbovee$ python join.py ./t1.csv ./t2.csv out.csv -k1 0 -k2 2
=====================
Entering importfile():
File:  ./t1.csv  Closed?  False  Mode  r
Len tbl= 0  table1= 0  table2= 0
--------------------
Entering procline for s:
A,B,C,D,E

key= 0  k= 5  key<k:  True
At append:
['A', 'B', 'C', 'D', 'E']
--------------------
Entering procline for s:
F,G,H,I,J

key= 0  k= 5  key<k:  True
At append:
['F', 'G', 'H', 'I', 'J']
--------------------
Entering procline for s:


=====================
Entering importfile():
File:  ./t2.csv  Closed?  False  Mode  r
Len tbl= 0  table1= 2  table2= 0
--------------------
Entering procline for s:
K,L,M,N,O,P,Q,R

key= 2  k= 8  key<k:  False
--------------------
Entering procline for s:
S,T,A,V,W,X,Y,Z

key= 2  k= 8  key<k:  False
--------------------
Entering procline for s:


In main():
Count table1= 2  table2= 0
Len table1= 2  table2= 0
sierra:join tbovee$ 

END ERROR DISCUSSION
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
#END get arguments

def procline(s,tbl,key,sep):
# Splits s into fields and inserts into appropriate lists
	if DEBUG == 1:
		print "--------------------"
		print "Entering procline for s:"
		print s
	s = s.rstrip()
	if len(s) > 0:
	  	curr = s.split(sep)
  		#k = len(curr)
		if DEBUG == 1: 
			print "key=",key," len(curr)=",len(curr)," key<len(curr): ",key<len(curr)
		if key < len(curr):
			if DEBUG == 1:
				print "At append:"
				print curr
			tbl.append(curr)
			s = ""
# END procline


def importfile(fileobj,tbl,key,sep,names):
# Reads file from disk and passes each line to procfile()
	if DEBUG == 1:
		print "====================="
		print "Entering importfile():"
		print "File: ",fileobj.name," Closed? ",fileobj.closed," Mode ",fileobj.mode
		print "Len tbl=",len(tbl)," table1=",len(table1)," table2=",len(table2)
	ptr = 0
	for line in fileobj :
		ptr = ptr + 1
		if ptr == 1:
			if names == False:
				procline(line,tbl,key,sep)
			#END if names....
		else:
			procline(line,tbl,key,sep)
		#END if pointer...
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
	global bigtable
	global bigkey
	global smalltable
	global smallkey
	global table1
	global table2
	global count1
	global count2
		
	F1 = open(file1, 'r')
	count1 = importfile(F1,table1,key1,sep1,names1)
	F1.close()
	F2 = open(file2, 'r')	
	count2 = importfile(F2,table2,key2,sep2,names2)
	F2.close()
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
	Truncating import tables to reclaim memory	
	'''
	#table1 = []
	#table2 = []
# END importfiles

def main() :
	importfiles()
	if DEBUG == 1:
		print "In main():"
		print "Count table1=",str(count1)," table2=",str(count2)
		print "Len table1=",len(table1)," table2=",len(table2)
		# END Test output
	return
#End main

# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--