#!/usr/bin/python 
# Filename: Main.py 

import Knapsack
# import Trackback

n = 5
c = 10 
w = [0, 2, 2, 6, 5, 4]
v = [0, 6, 3, 5, 4, 6]

m = []
for i in range(0, n + 1): 
  m.append([])
  for j in range(0, c + 1):
    m[i].append(0)

x = []
for i in range(0, n + 1):
  x.append(0)

Knapsack.Knapsack(v, w, c, n, m)

Knapsack.Traceback(m, w, c, n, x)

print m
print x

print m[1][c]
