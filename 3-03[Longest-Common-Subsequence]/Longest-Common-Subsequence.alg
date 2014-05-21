LCSLength(m, n, arrayX, arrayY, c, b)
	for i = 1 to m + 1
		for j = 1 to n + 1
			if arrayX[i] == arrayY[j]
				c[i][j] = c[i - 1][j - 1] + 1
				b[i][j] = 1
			else if c[i - 1][j] >= c[i][j - 1]
				c[i][j] = c[i - 1][j]
				b[i][j] = 2
			else
				c[i][j] = c[i][j - 1]
				b[i][j] = 3


LCS(i, j, arrayX, b)
	if i == 0 or j == 0
		return 
	if b[i][j] == 1
		LCS(i - 1, j - 1, arrayX, b)
		print arrayX[i]
	else if b[i][j] == 2
		LCS(i - 1, j, arrayX, b)
	else
		LCS(i, j - 1, arrayX, b)
