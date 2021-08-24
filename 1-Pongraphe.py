import numpy as np

def insertionSort(B): 
    for j in range (1,len(B)):   #j is like a index start at 1 to compare(0) the the first value 
        key = B[j]          #key is the current indicator 
        i=j-1               #i is like a position 
        while i>=0 and B[i]<=key:  # When i is more than 0 and key is more, insert the value of the current B[i] to the next array. 
            B[i+1]=B[i]
            i=i-1
        # When array B is more, insert the value of key into the element     
        B[i+1]=key
    return B       



def merge(A,p,q,r):
    # Create new array 
    L = A[p:q]
    R=  A[q:r+1]
    # Add infinite at the end to copy everything 
    L = np.append(L,np.inf)
    R = np.append(R,np.inf)
    # To merge the array back to A 
    i = 0   # To indicate index of first subarray at 0
    j = 0   # To indicate index of second subarray at 0
    
    for k in range(p,r+1):
    # When the value of L is less or equal, insert value of L into A then i is incremented 
        if (L[i] <= R[j]):
            A[k] = L[i]
            i = i+1
        else:
    # When the value of R is less or equal, insert value of R into A then j is incremented 
            R[j] <= L[i]
            A[k] = R[j]
            j = j+1
            
    return A
# sub-array of A is to be sorted
def mergeSort(A,p,r):

    if p<r:
        # floor division (round it down) 
        q = (p+r)//2
        # Sort the left array A
        mergeSort(A,p,q)
        # Sort the right array A
        mergeSort(A,q+1,r)
        # combine the array to A 
        merge(A,p,q+1,r)
    return A

A = np.random.randint(10,size=10)
B = np.random.randint(10,size=10)
print("Sample B:",B)
print("Insertion Sort:",insertionSort(B))
print("Sample A:",A)
print("Merge Sort:",mergeSort(A,0,len(A)-1))
