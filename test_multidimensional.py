#! /usr/bin/env python

# Import modules
import sys

recs = []

def main() : 
  a = ['A'],["this land is my land"]
  b = ['B'],["and our land"]
  
  recs.append(a)
  recs.append(b)
  first = str(recs[0][1])
  first = first.strip(["[","]"])
  print first
  sys.exit()
  print str(recs[0][1])
  print recs[1][1]
  print str(str(recs[0][1]) + str(recs[1][1]))
  

  
  

# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--