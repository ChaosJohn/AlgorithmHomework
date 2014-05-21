#!/usr/bin/python
# Filename: Randomized-Select.py

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
     
def RandomizedSelect(array, p, r, k):
	if 	p == r:
		return array[p]
	i = RandomizedPartition(array, p, r)
	j = i - p + 1
	if 	k <= j:
		return RandomizedSelect(array, p, i, k)
	else:
		return RandomizedSelect(array, i + 1, r, k - j);


num = int(raw_input("Please input the number of elements in the random-created array: "))

array = [random.randint(1, 10000) for i in range(0, num)]

print "\nThe random-created array: " 

for i in range(0, num):
	if i % 10 == 0:
		print
	print str(array[i]) + '\t', 
print

selectNum = int(raw_input("\nPlease input the ____th minimum element to select: "))

print "The " + str(selectNum) + "th minimum element is: ", 
print RandomizedSelect(array, 0, num - 1, selectNum)

print
