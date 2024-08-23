#!/usr/bin/env python3

def reverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1



def leftRotate(arr, d):
    if d == 0:
        return
    n = len(arr)

    # in case the rotating factor is greater than array length then rotate it by taking modulo of array length
    d = d % n

    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)


def printArray(arr):
    for i in range(0, len(arr)):
        print (arr[i],end=' ')


#Driver functions for printing the array
arr = [1, 2, 3, 4, 5, 6, 7]
print ("Original array is:")
printArray(arr)

leftRotate(arr, 2) # Rotate array by 2
print ("\nArray after left rotation by 2:")
printArray(arr)

leftRotate(arr, 3) # Rotate array by 3
print ("\nArray after left rotation by 3:")
printArray(arr)

leftRotate(arr, 4) # Rotate array by 4
print ("\nArray after left rotation by 4:")
printArray(arr)

# Time complexity: O(n)
# Space complexity: O(1)