#!/usr/bin/python 
# Filename: Main.py 

import FlowShop 

a = [5, 12, 4, 8]
b = [6, 2, 14, 7]
c = []
for i in range(0, 4):
  c.append(-1)

k = FlowShop(4, a, b, c)

print k
