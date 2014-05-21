#!/usr/bin/python 
# Filename: Main.py 

import Huffman_Codes

array = []
a = []
array.append(Huffman_Codes.node('a', 45))
array.append(Huffman_Codes.node('b', 13))
array.append(Huffman_Codes.node('c', 12))
array.append(Huffman_Codes.node('d', 16))
array.append(Huffman_Codes.node('e', 9))
array.append(Huffman_Codes.node('f', 5))
for i in range(0, 5): 
  array.append(Huffman_Codes.node())

Huffman_Codes.Huffman_Codes(array)

Huffman_Codes.Traceback(array, len(array) - 1, a)
