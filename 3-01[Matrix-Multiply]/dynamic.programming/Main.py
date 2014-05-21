#!/usr/bin/python 
# Filename: Main.py 

import MatrixChain

p = [30, 35, 15, 5, 10, 20, 25]
n = 7
m = []
for i in range(0, n):
  m.append([])
  for j in range(0, n): 
    m[i].append(-1)

s = []
for i in range(0, n):
  s.append([])
  for j in range(0, n):
    s[i].append(-1)


MatrixChain.MatrixChain(p, 6, m, s)
MatrixChain.Traceback(1, 6, s)

#print m
