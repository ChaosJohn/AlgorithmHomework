#!/usr/bin/python 
# Filename: Knapsack.py 

def min(a, b):
  if a < b:
    return a
  else: 
    return b

def max(a, b): 
  if a > b: 
    return a
  else: 
    return b

def Knapsack(v, w, c, n, m): 
  jMax = max(w[n] + 1, c)
  for j in range(0, jMax + 1):
    m[n][j] = 0
  for j in range(w[n], c + 1): 
    m[n][j] = v[n]
  for i in range(n - 1, 1, -1):
    jMax = min(w[i] - 1, c)
    for j in range(0, jMax + 1):
      m[i][j] = m[i + 1][j]
    for j in range(w[i], c + 1):
      m[i][j] = max(m[i + 1][j], m[i + 1][j - w[i]] + v[i])

  m[1][c] = m[2][c]
  if c >= w[1]: 
    m[1][c] = max(m[1][c], m[2][c - w[1]] + v[1])

def Traceback(m, w, c, n, x):
  for i in range(1, n): 
    if m[i][c] == m[i + 1][c]: 
      x[i] = 0
    else: 
      x[i] = 1
      c = c - w[i]
  x[n] = 1 if m[n][c] != 0 else 0
