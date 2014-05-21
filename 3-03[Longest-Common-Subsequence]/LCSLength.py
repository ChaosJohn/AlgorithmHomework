#!/usr/bin/python
# Filename: LCSLength.py

import random

def LCSLength(m, n, arrayX, arrayY, c, b):
	'''
	for	i in range(0, m + 1):
		c[i][0] = 0
	for	i in range(0, n + 1):
		c[0][i] = 0
	'''
	for i in range(1, m + 1):
		for	j in range(1, n + 1):
			if	arrayX[i] == arrayY[j]:
				c[i][j] = c[i - 1][j - 1] + 1
				b[i][j] = 1
			elif c[i - 1][j] >= c[i][j - 1]:
				c[i][j] = c[i - 1][j]
				b[i][j] = 2
			else:
				c[i][j] = c[i][j - 1]
				b[i][j] = 3

