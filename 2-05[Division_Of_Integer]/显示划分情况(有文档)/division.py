#!/usr/bin/python
# Filename: division.py

array = [0 for i in range(0, 100)]
amount = 0

def Output(num):
	global amount
	for i in range(0, num):
		print array[i],
	amount += 1
	print

def Division(Max, Index):
	if Max == 0:
		Output(Index)
	else:
		for i in range(Max, 0, -1):
			if Index == 0 or i <= array[Index - 1]:
				array[Index] = i
				Division(Max - i, Index + 1)

Input = int(raw_input("Please enter a nonnegative integer: "))
Division(Input, 0)
print '\t' + str(amount) + ' ways of division\n'
