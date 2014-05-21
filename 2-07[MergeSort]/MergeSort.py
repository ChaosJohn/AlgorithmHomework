#!/usr/bin/python
# Filename: MergeSort.py

import random

def MergeSort(A, B, left, right):
	if left < right:
		i = (left + right) / 2
		MergeSort(A, B, left, i)
		MergeSort(A, B, i + 1, right)
		Merge(A, B, left, i, right)
		Copy(A, B, left, right)

def Copy(new, old, left, right):
	for i in range(left, right + 1):
		new[i] = old[i]
	
def Merge(A, B, left, i, right):
	AL = [A[j] for j in range(left, i + 1)]
	AL.append(0)
	AR = [A[j] for j in range(i + 1, right + 1)]
	AR.append(0)
	Bindex = left
	Lindex = Rindex = 0
	while 1:
		if AL[Lindex] == 0:
			for j in range(Rindex, len(AR) - 1):
				B[Bindex] = AR[j]
				Bindex += 1
			break
		elif AR[Rindex] == 0:
		  	for j in range(Lindex, len(AL) - 1):
				B[Bindex] = AL[j]
				Bindex += 1
			break
		elif AL[Lindex] < AR[Rindex]:
		  	B[Bindex] = AL[Lindex]
		  	Bindex += 1
		  	Lindex += 1
		  	continue
		elif AL[Lindex] >= AR[Rindex]:
		  	B[Bindex] = AR[Rindex]
		  	Bindex += 1
		  	Rindex += 1
		else:
		  	pass

input = int(raw_input("Please input the number of elements in the random-created array: "))

A = [random.randint(1, 100000) for i in range(0, input)]

B = [0 for i in range(0, input)]

print "The random array before sorted: \n", 
for i in range(0, input):
	if i % 10 == 0:
		print
	print str(A[i]) + '\t',
print

MergeSort(A, B, 0, input -1)

print "\n---------------------------------------------\n\nThe sorted array: \n", 
for i in range(0, input):
	if i % 10 == 0:
		print
	print str(A[i]) + '\t', 
print
