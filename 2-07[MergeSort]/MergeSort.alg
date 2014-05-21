MergeSort(A, B, left, right) 
	if left < right
		i = (left + right) /2
		MergeSort(A, B, left, i)
		MergeSort(A, B, i + 1, right)
		Merge(A, B, left, i, right)
		Copy(A, B, left, right)
