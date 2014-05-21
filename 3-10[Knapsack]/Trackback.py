def Traceback(m, w, c, n, x):
  for i in range(1, n): 
    if m[i][c] == m[i + 1]: 
      x[i] = 0
    else: 
      x[i] = 1
      c = c - w[i]
  x[n] = 1 if m[n][c] != 0 else 0