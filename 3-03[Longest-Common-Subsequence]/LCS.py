#!/usr/bin/python
# Filename: LCS.py

def LCS(i, j, arrayX, b):
	if	i == 0 or j == 0:
		return
	if 	b[i][j] == 1:
		LCS(i - 1, j - 1, arrayX, b)
		print arrayX[i]
	elif b[i][j] == 2:
		LCS(i - 1, j, arrayX, b)
	else: 
		LCS(i,j - 1, arrayX, b)
