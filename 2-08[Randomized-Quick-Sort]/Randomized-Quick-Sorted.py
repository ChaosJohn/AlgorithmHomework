#!/usr/bin/python
# Filename: Randomized-Quick-Sort.py

import random

def RandomizedPartition(array, p, r):
	index = random.randint(p, r + 1)
	base = array[index]
	a = [0]
	b = [0]
	
	for i in range(p, r + 1):
		if i == index:
			continue
		elif array[i] <= base:
			a.append(array[i])
		elif array[i] > base:
			b.append(array[i])
		else:
			pass

	x = p
	
	for i in range(1, len(a)):
		array[x] = a[i]
		x += 1
	
	array[x] = base
	q = x
	x += 1

	for i in range(1, len(b)):
		array[x] = b[i]
		x += 1

	return q

def RandomizedQucikSort(array, p, r):
	if	p < r:
		q = RandomizedPartition(array, p, r)
		RandomizedQucikSort(array, p, q - 1)
		RandomizedQucikSort(array, q + 1, r)

num = int(raw_input("Please input the number of elements in the random-created array: "))

array = [random.randint(1, 10000) for i in range (0, num)]

print "The random array before sorted: \n", 
for i in range(0, num):
  	if i % 10 == 0:
		print
	print str(array[i]) + '\t',
print

RandomizedQucikSort(array, 0, num - 1)

print "\n---------------------------------------------\n\nThe sorted array: \n", 
for i in range(0, num):
  	if i % 10 == 0:
		print
	print str(array[i]) + '\t', 
print
