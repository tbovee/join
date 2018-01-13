#! /usr/bin/env python

# Import modules
import sys

recs = []

def main() : 
  a = 1,2,3,4,5
  b = 6,7,8,9,10
  c = 11,12,13,14,15,a
  d = 16,17,18,19,20,b
  
  recs.append(a)
  recs.append(b)
  recs.append(c)
  print recs[0]
  print recs[1]
  print recs[2]
  print recs[2][5][3]

  
  

# CALL MAIN

if __name__ == '__main__' :
  main()

# --EOF--