#!/usr/bin/env python

import sys

pattern = sys.argv[1]
filename = sys.argv[2:]
ticktock=0
while ticktock != len(filename):
   with open(filename[ticktock]) as f:
      a = f.readlines()
   
   i = 0
   while i < len(a):
      s=a[i]
     
      j=0
      while j < len(s) and s[j:j+len(pattern)] != pattern:
         j = j + 1
      
      if j <len(s):
         print s.rstrip()

      i = i + 1
   ticktock=ticktock+1