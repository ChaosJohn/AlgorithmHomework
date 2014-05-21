#!/usr/bin/python 
# Filename: Memoried.py 

def MemoriedMatrixChain(n, m, s, p): 
  for i in range(1, n + 1):
    for j in range(i, n + 1): 
      m[i][j] = 0
  return LookupChain(1, n, m, s, p)


def LookupChain(i, j, m, s, p):
  if m[i][j] > 0: 
    return m[i][j]
  if i == j: 
    return 0 
  u = LookupChain(i, i, m, s, p) + LookupChain(i + 1, j, m, s, p) + p[i - 1] * p[i] * p[j]
  s[i][j] = i
  for k in range(i + 1, j): 
    t = LookupChain(i, k, m, s, p) + LookupChain(k + 1, j, m, s, p) + p[i - 1] * p[k] * p[j]
    if t < u: 
      u = t
      s[i][j] = k
  m[i][j] = u
  return u

def Traceback(i, j, s):
  if i == j: 
    return 
  Traceback(i, s[i][j], s)
  Traceback(s[i][j] + 1, j, s)
  print 'Multiply A', i, ',', s[i][j], 
  print 'and A', s[i][j] + 1, ',', j