import time
import matplotlib.pyplot as plt
from statistics import mean

"""
 Bucket Sort: Under assumption of a uniform distribution and independent input.
 A is the input 
"""

def insertionSort(b):
    for j in range (1,len(b)):
        key = b[j]
        i = j-1
        while i>=0 and b[i]>=key:
            b[i+1]=b[i]
            i -= 1
        b[i+1]=key
    return b
 
def bucket_sort(A) :
    # make Bucket
    num_bucket = 10 # 10 mean 10 slots each in decimal. 
    arr = []
    for i in range(0,int(num_bucket)):
        arr.append([])

    # insert into the Bucket
    for j in A:
        index_A = int(num_bucket*j)
        arr[index_A].append([j])
        
    #print("arr insert:", arr)     
    # Insertion sort on each slots
    for i in range(int(num_bucket)):
         insertionSort(arr[i])

    # Concate all slot in the bucket
    sorted_output = []
    for i in range(0,int(num_bucket)):
        sorted_output.extend(arr[i])
    return sorted_output
    
A = [0.78,0.17,0.39,0.26,0.72,0.94,0.21,0.12,0.23,0.68]
start = time.time()    
print("Sorted Bucket:\n", bucket_sort(A))
end = time.time()
diff = round(end -start,ndigits=4)
print("Bucket Time: %-sS"%(diff))


"""
Quick sort: sorts in place
Counting sort(Stable sort): use temporary storage such as C ,B list 
Radix sort: need stable sort to sort the digit. 

"""

def countingSortForRadix(inputArray, getIndex):
    
    k = 10
    counts = [0]*k 
    # Sort inputArray
    # Base is the getIndex 
    # Counting O(n)
    for i in range(len(inputArray)):
        tempSpace = (inputArray[i] // getIndex) % 10
        counts[tempSpace] += 1
    
    # Accumulating O(k)
    # The sum of the elements less than x
    for i in range (1,10):
        counts[i] = counts[i] + counts[i-1]
    output = [0]*len(inputArray) 
    # Calculation start index O(k)
    # Put the sorted value into the output array
    for i in range (len(inputArray) -1,-1,-1):
        tempSpace = (inputArray[i] // getIndex)%10
        output[counts[tempSpace]-1] = inputArray[i]
        counts[tempSpace] = counts[tempSpace] - 1
    return output

def getDigit(num,d):
    # Get Digit d in the number num 
    # Floor division //    
    for i in range (d -1):
        num = num // 10
    return num % 10 
#print(num)

def radixSort(inputArray):
    max_value = max(inputArray) # The max value in the input array 
    getIndex = 1                # The beginning base of the Least Significant bit(LSB)
    output = inputArray         # Create output to be the same as input array 
    for d in range(len(str(max_value))):  # Looping the max value number 
        output = countingSortForRadix(output,getIndex) # Sorting
        getIndex = getIndex*10              # Increase the base by 10 
    return output 
        
array = [462,273,1465,722,383,159,1478,1234,6547,753,852,632]
start = time.time() 
s = radixSort(array)
print("Sorted Radix:\n",s) 
end = time.time()
diff = round(end -start,ndigits=10)
print("Radix Time: %-sS"%(diff))

    
        
#Quick Sort
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

    
B = [15,13,9,5,12,8,7,4,0,6,2,1]
n = len(B)
start = time.time() 
QuickSort(B,0,n-1)
print("QuickSort:\n{}".format(B)) 
end = time.time()
diff = round(end -start,ndigits=10)
print("QuickSort Time: %-sS"%(diff))


        
