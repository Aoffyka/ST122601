import numpy as np
import matplotlib.pyplot as plt
import time
start_time = time.time()

# Recursive fuction to find the maximum contiguous subarray 
def MaxSubArray(A,low,high):
    if high == low :
        return low,high,A[low] # if the current array only has one element, then return it 
    else:
        mid = (low + high)//2 #mid index for the current array 
        left_low, left_high, left_sum = MaxSubArray(A,low,mid)  # Create New array (from index 0 to the current mid index) and run the function.
        right_low, right_high, right_sum = MaxSubArray(A,mid+1,high) # Create New array (from the current mid index to the end index) and run the function.
        cross_low, cross_high, cross_sum = MaxCrossSubArray(A,low,mid,high) # Find the maximum sum of the current mid-crossing subarray. 
    #  From start and end indexes of sum and return the maximum sum    
    if (left_sum > right_sum and left_sum > cross_sum):
            return left_low, left_high, left_sum
    elif (right_sum > left_sum and right_sum > cross_sum):
            return right_low, right_high, right_sum
    else:
            return cross_low, cross_high, cross_sum

# A Function to find maximum sum of the current mid crossing subarray 
def MaxCrossSubArray(A,low,mid,high):
    # To make sure that the first in the array can always be replacable for the left 
    sum_left = float('-inf')
    total = 0
    max_left = 0
    # Find the max sum on the left (from mid to low) 
    for i in range(mid, low-1,-1):              # Loop through the left array
        total += A[i]                           # Add current index's value to total
        if total > max_left:                    # If the total is higher than the former sum
            sum_left = total                    # Set the max left sum to be equal to the current sum
            max_left = i                        # Set the start index to be the current index(I)
    # To make sure that the first in the array can always be replacable for the right 
    sum_right = float('-inf')
    total = 0
    max_right = 0
    # Find the max sum on the right (mid to high) 
    for j in range(mid+1, high+1):              # Loop through the right array
        total += A[j]                           # Add current index's value to total 
        if total > sum_right:                   # If the total is higher than the former sum  
            sum_right = total                   # Set the max right sum to be equal to the current sum
            max_right = j                       # Set the end index to be the current index(J)
    return max_left, max_right, (sum_left+sum_right) # Return the sum with Start and end index (Start,End,SUM) 

A = [-5,1,2,9,-5,8]

StartIndex = 0
EndIndex = len(A)-1 

Start,End,Sum= MaxSubArray(A, StartIndex, EndIndex)
print("The Array:",A)
print("The Subarray:",A[Start:End+1])
print (Start,End,"The SUM:",Sum)

TimeTaken = time.time() - start_time

print(" %s seconds" % (TimeTaken))


# x axis values
x = np.logspace(0,15,100,dtype=np.longdouble)

y_nlogn = (1/500000)*x*np.log(x) 

fig = plt.figure()
p = fig.add_subplot(1,1,1)
p.set_yscale('log')
p.set_xscale('log')
p.set_xlim(1,10**15)
p.set_ylim(1,10**19)

p.plot(x,y_nlogn,label='nlogn')

p.legend()
plt.xlabel('Time')
plt.ylabel('n')
plt.title('Function')
plt.show()

