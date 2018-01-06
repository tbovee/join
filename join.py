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

def importFile() :
  Fleft = open (tableleft', 'rU')
  for line in Fleft :
  	# Split into fields
  	### How do I show curr to be an array
  	curr = line.split(delimleft)
  	### check use of len
  	# Save the number of fields
  	k = len(curr)
  	
def scanFright) :
  

def main() : 
  print "Howdy, Pardner!"
  
  

# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--