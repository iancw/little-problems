# Sorts ar in place using quicksort algorithm
def heapsort(ar):
	pass

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

