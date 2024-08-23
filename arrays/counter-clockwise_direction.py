#!/usr/bin/env python3

#Function to rotate an array by d elements in counter-clockwise direction. 
def rotateArr(A,D,N):
    #Your code here
    A[:]=A[D%N:]+A[:D%N]
    return A

#Driver code to test above function
arr = [1, 3, 5, 7, 9]
print ("Original array is:", arr)

d = 2
n = len(arr)
arr = rotateArr(arr, d, n)
print ("Array after left rotation by", d, "elements is:", arr)

# Time complexity: O(n)
# Space complexity: O(1)
        