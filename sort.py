from heap import heap
# Sorts ar in place using quicksort algorithm
def heapsort(ar):
	h = heap()
	for e in ar:
		h.insert(e)
	r = []
	for i in range(0, len(ar)):
		r.append(h.extract_min())
	return r

def merge(a, b):
	out = []
	i = 0
	j = 0
	while i < len(a) and j < len(b):
		if a[i] < b[j]:
			out.append(a[i])
			i = i + 1
		else:
			out.append(b[j])
			j = j + 1
	if i < len(a):
		out.extend(a[i:])
	else:
		out.extend(b[j:])
	return out

# Sorts array in place using mergesort algorithm
def mergesort(ar):
	if len(ar) <= 1:
		return ar
	# divide array in half...
	m = len(ar) / 2
	a = mergesort(ar[:m])
	b = mergesort(ar[m:])
	return merge(a, b)

def swap(ar, i, j):
	t = ar[i]
	ar[i] = ar[j]
	ar[j] = t

def quicksort(ar):
	_quicksort(ar, 0, len(ar)-1)

def partition(ar, l, h):
	p = h
	firsthigh = l
	for i in range(l, h):
		if ar[i] < ar[firsthigh]:
			swap(ar, i, firsthigh)
			firsthigh += 1
	swap(ar, p, firsthigh)
	return firsthigh



def _quicksort(ar, l, h):
	if h-1 > 0:
		p = partition(ar, l, h)
		_quicksort(ar, l, p-1)
		_quicksort(ar, p+1, h)

	
