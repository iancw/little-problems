# Sorts ar in place using quicksort algorithm
def quicksort(ar):
	pass

# Sorts array in place using mergesort algorithm
def mergesort(ar):
	if len(ar) is 1:
		return ar
	if len(ar) is 0:
		return ar
	# divide array in half...
	m = len(ar)/2
	a = mergesort(ar[:m])
	b = mergesort(ar[m:])

