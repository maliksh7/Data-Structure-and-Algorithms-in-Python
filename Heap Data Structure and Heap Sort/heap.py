def heapify(lst,length,root):
	n = root

	largest = root
	l = 2*n + 1
	r = 2*n +2

	if l < length and lst[l] > lst[largest]:
		largest = l                                #update largest

	if r < length and lst[r] > lst[largest]:
		largest = r                                #update largest

	if largest != n:
		lst[n] , lst[largest] = lst[largest] , lst[n]  #swap

		heapify(lst,length,largest)

def build_heap(lst):
	n = len(lst)

	for i in reversed( range( n // 2 ) ):
		heapify(lst,n,i)

def heap_sort(lst):
	n = len(lst)
	
	build_heap(lst)

	for i in reversed(range(n)):
		lst[i] , lst[0] = lst[0] , lst[i]   #swap

		heapify(lst,i,0)


heap = [100, 5, 3, 2, 8, 15, 6, 102]
print("Heap List: ", heap)
build_heap(heap)
print("Build Heap: ", heap)
heap_sort(heap)
print("Sorted Heap: ", heap)