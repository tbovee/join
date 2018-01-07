#! /usr/bin/env python

# A learning project to learn python, just for me.
'''
Program join imports two files 
	in the csv format (no quotes around strings) 
	with a single key column
It reads file "Fleft", which will typically be the smallest table,
and then selects each matching record from file "Fright'.
It will combine all of the fields in Fleft with all of the fields, excepting the key field,
from Fright.

Needed vVariables

tableleft string
tableright string
keyleft integer
keyright integer
delimleft integer
delimright integer
colnames boolean
kleft integer
kright integer


Commandline 
join [parameters]
parameters =
-tl tableleft
-tr tableright
-kl keyleft
-kr keyright
-dl delimleft
-dr delimright
-cn  colnames

'''

# Command line arguments

# Global names
kleft = 0
kright = 0

# Import modules
import sys
# import pandas as pd

def getargs():
	n = len(sys.argv)-1
	for i in range(0,n):
		if sys.argv[i] = '-tl':
			tableleft = sys.argv[i+1]
		elif sys.argv[i] = '-tr':
			tableright = sys.argv[i+1]
		elif sys.argv[i] = '-kl':
			keyleft = sys.argv[i+1]
		elif sys.argv[i] = '-kr':
			keyright = sys.argv[i+1]
		elif sys.argv[i] = '-dl':
			delimleft = sys.argv[i+1]
		elif sys.argv[i] = '-dr':
			delimright = sys.argv[i+1]
		elif sys.argv[i] = '-cn':
			cn = sys.argv[i+1]
			if cn = 1:
				colnames = True
			else
				colnames = False
# END getargs			
		
	

# End args

def importfile(table,delim,key,k) :
  F = open (table, 'r')
  first = 0
  for line in F :
	  	# Split into fields
  	curr = line.split(delim)
	  	# Save the number of fields
  	if first == 0:
  		k = len(curr)
  		first = 1
  		# Test lioness
  	print curr
  		# End Test
# End importfile


def main() :

	  # Test run
	tableleft = "./tl.csv"
	tableright = "./tr.csv"
	keyleft = 1
	keyright = 3
	delimleft = ","
	delimright = ","
	colnames = False

	importfile(tableleft,",",1,kleft)
	importfile(tableright,",",3,kright)
	
	return
		# End Test  
#End main

# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--