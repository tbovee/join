#! /usr/bin/env python

# project as part of my learning python, restricted to the built-ins
# Version 20180107.1355

'''
Program join imports two files 
	in the csv format (no quotes around strings) 
	with a single key column
It reads file "Fleft", which will typically be the smallest table,
and then selects each matching record from file "Fright'.
It will combine all of the fields in Fleft with all of the fields, excepting the key field,
from Fright.

Invoke:

join.py -type -value [type value ...]

'''

'''
QUESTION TO RESEARCH: I need an array of arrays for each table to most efficiently compare them.

And it appears not to be possible

SOLUTION: 

Create symlists symleft, symright, ptrleft, ptrright
Within def importfile save the field containing the stock symbol in symleft or symright, 
depending upon the table, and the line number (count withi the file excluding the
colnames) to ptrleft and ptrright, respectively.

In doing the join, 
	For reach item in one symlist , check the other symist for a matching symbol, 
	and get the line number from the target ptrlist. Reach the target file until
	the line number in ptrllist is reached, then capture the data from both files.
	
	Intuitively, I think it makes most since to the longest table to be the source
	file and the shortest the target, since the target must be read multiple times.
	
	Is a ptrlist needed for the source table? Probably not,
	
	The sourcetable should be designatable in the command line.
	

'''




# Command line arguments

# Global names
fileleft = ""
fileright = ""
keyleft = 0
keyright = 0
delimleft = ","
delimright = ","
colnames = False
kleft = 0
kright = 0

# Import modules
import sys
# import pandas as pd


n = len(sys.argv)-1
for i in range(0,n):
	if sys.argv[i] == '-tl':
		fileleft = sys.argv[i+1]
	elif sys.argv[i] == '-tr':
		fileright = sys.argv[i+1]
	elif sys.argv[i] == '-kl':
		keyleft = sys.argv[i+1]
	elif sys.argv[i] == '-kr':
		keyright = sys.argv[i+1]
	elif sys.argv[i] == '-dl':
		delimleft = sys.argv[i+1]
	elif sys.argv[i] == '-dr':
		delimright = sys.argv[i+1]
	elif sys.argv[i] == '-cn':
		cn = sys.argv[i+1]
		if cn == 1:
			colnames = True
		else:
			colnames = False


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