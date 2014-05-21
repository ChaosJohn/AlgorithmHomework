RandomizedPartition(array, p, r)
	index = Random(p, r)
	base = array[index]
	create array 'a[]'
	create array 'b[]'

	for i = p to r + 1
		if i == index
			continue
		else if array[i] <= base:
			copy array[i] to a[]
		else 
			copy array[i] to b[]

	x = p
	for i = 1 to a.length
		array[x] = a[i]
		x += 1
	array[x] = base
	q = x
	x += 1
	for i = 1 to b.length
	 	array[x] = b[i]
		x += 1

	return q


RandomizedQuickSort(array, p, r):
	if p < r
		q = RandomizedPartition(array, p, r)
		RandomizedQuickSort(array, p, r)
		RandomizedQuickSort(array, p, r)
