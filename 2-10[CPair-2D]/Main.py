#!/usr/bin/python 
# Filename: Main.py 

import CPair 
import random

pointCount = 10 

print '\n----------------------------------------------------\n'
print 'The randomized points is listed as follows: '
points = [] 
for i in range(0, pointCount): 
  points.append(CPair.PointX(i, random.randint(1, 100), random.randint(1, 100))) 
  print '[', points[i].x, ',', points[i].y, ']' 

List = [CPair.PointX(), CPair.PointX(), -1]
CPair.CPair(points, pointCount, List) 
print '\nThe closest pair of points are [', List[0].x, ',',  List[0].y, '] & [',  List[1].x, ',',  List[1].y, '], and the distance is',  List[2]
print '\n----------------------------------------------------\n'
