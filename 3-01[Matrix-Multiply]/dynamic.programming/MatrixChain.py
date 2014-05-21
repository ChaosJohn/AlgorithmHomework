#!/usr/bin/python 
# Filename: MatrixChain.py 

def MatrixChain(p, n, m, s): 
  for i in range(1, n + 1): 
    m[i][i] = 0;
  for r in range(2, n + 1): 
    for i in range(1, n - r + 2): 
      j = i + r - 1
      m[i][j] = m[i + 1][j] + p[i - 1] * p[i] * p[j]
      s[i][j] = i
      for k in range(i + 1, j): 
        t = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
        if t < m[i][j]: 
          m[i][j] = t
          s[i][j] = k

def Traceback(i, j, s):
  if i == j: 
    return 
  Traceback(i, s[i][j], s)
  Traceback(s[i][j] + 1, j, s)
  print 'Multiply A', i, ',', s[i][j], 
  print 'and A', s[i][j] + 1, ',', j
