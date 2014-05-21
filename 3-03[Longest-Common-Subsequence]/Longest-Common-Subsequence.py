#!/usr/bin/python
# Filename: Longest-Common-Subsequence.py

import random 
import LCSLength
import LCS

arrayX = [0, 'a', 'b', 'c', 'b', 'd', 'a', 'b']
arrayY = [0, 'b', 'd', 'c', 'a', 'b', 'a']

m = len(arrayX) - 1
n = len(arrayY) - 1

c = []
b = []

for i in range(0, m + 1):
	c.append([])
	for j in range(0, n + 1):
		c[i].append(0)

for i in range(0, m + 1):
	b.append([])
	for j in range(0, n + 1):
		b[i].append(0)

LCSLength.LCSLength(m, n, arrayX, arrayY, c, b)
LCS.LCS(m, n, arrayX, b)	
