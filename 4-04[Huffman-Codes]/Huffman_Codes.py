#!/usr/bin/python 
# Filename: Huffman_Codes.py 

class node:
  def __init__(self, flag = '', value = -1, left=-1, right = -1, prefix = -1):
    self.flag = flag 
    self.value = value
    self.left = left 
    self.right = right 
    self.prefix = prefix

def Huffman_Codes(array): 
  low = 0
  high = (len(array) - 1) / 2

  while low < high: 
    sort(array, low, high)
    high += 1
    array[high].value = array[low].value + array[low + 1].value 
    array[high].left = low 
    array[high].right = low + 1
    array[low].prefix = 0
    array[low + 1].prefix = 1
    low += 2

def Traceback(array, index, a):
  if array[index].left != -1: 
    a.append(0)
    Traceback(array, array[index].left, a)
    a.pop()
    a.append(1)
    Traceback(array, array[index].right, a)
    a.pop()
  else: 
    print str(a) + ' ==> ' + array[index].flag + '(' + str(array[index].value) + ')' 

def sort(array, a, b): 
  for i in range(a, b): 
    k = i
    for j in range(i + 1, b + 1): 
      if array[j].value < array[k].value: 
        k = j
    if k != i: 
      temp = node()
      temp = array[i]
      array[i] = array[k]
      array[k] = temp 
