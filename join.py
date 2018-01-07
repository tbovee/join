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
-n  colnames

'''


 

# Import modules
import sys
# import pandas as pd

def importfile(table,delim,key,k) :
  Fleft = open (table', 'rU')
  first = 0
  for line in F :
	  	# Split into fields
  	curr = line.split(delim)
	  	# Save the number of fields
  	if first = 0:
  		k = len(curr)
  		first = 1
  		# Test lioness
  	print curr
  		# End Test
# End importfile


def main() : 
	  # Test run
	tableleft = "tl.csv"
	tableright = "tr.csv"
	keyleft = 1
	keyright = 3
	delimleft = ","
	delimright = ","
	colnames = False

	importfile()
	return
		# End Test  
#End main

# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--