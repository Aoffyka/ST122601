
#Heap Sort

def left(i):
    return (2*i+1)

def right(i):
    return (2*i+2)

#Run time: o(lgn)~o(n)
def build_max_heap(A):
    for i in range((len(A)-1)//2, -1, -1):
        max_heapify(A, i, len(A))
    
#Run time: o(lgn)~o(n)       
def max_heapify(A,i,heap_size):
    l = left(i)
    r = right(i)
    if (l < heap_size and A[l] > A[i]):
        largest = l
    else:
        largest = i
    if (r < heap_size and A[r] > A[largest]):
        largest = r
    if (largest != i):
        A[largest], A[i] = A[i], A[largest]
        max_heapify(A, largest, heap_size)

#Run time: o(nlgn)        
def heapsort(A):
    build_max_heap(A)
    print("Heap: \n{}".format(A))
    heap_size = len(A)
    for i in range(len(A) - 1,0,-1):
        # swap A[0] (root) with A[i]
        #A[0],A[i] = A[i],A[0] Do the exchange 
        temp = A[i] # Last to temp  
        A[i] = A[0] # First to last 
        A[0] = temp # temp to first 
        heap_size -= 1
        max_heapify(A,0,heap_size)


#Quick Sort: Noted Can use insertion sort
#Run time: o(lgn)~o(n) 
def partition(B,first,last):
    x = B[last]
    i = first 
    for j in range(first,last):
        if (B[j] <= x):
            B[i],B[j] = B[j],B[i]
            i += 1
    B[i],B[last] = B[last],B[i]
    return (i) 
#Run time: o(nlgn)  
def QuickSort(B,first,last):
    if (first < last):
        mid = partition(B,first,last)
        QuickSort(B,first,mid-1)
        QuickSort(B,mid+1,last)

A = [5,13,2,25,7,17,20,8,4]
heapsort(A)
print("HeapSort:\n{}".format(A))
B = [15,13,9,5,12,8,7,4,0,6,2,1]
n = len(B)
QuickSort(B,0,n-1)
print("QuickSort:\n{}".format(B))

    
