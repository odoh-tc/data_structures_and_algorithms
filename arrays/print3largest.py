#!/usr/bin/env python3

def print3largest(arr):

    arr_size = len(arr)

    if arr_size < 3:
        print("Invalid Input")
        return
    
    third = first = second = float('-inf')

    for i in range(arr_size):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            third = second
            second = arr[i]
        elif arr[i] > third and arr[i] != second and arr[i] != first:
            third = arr[i]


    print("Three largest elements are", first, second, third)


# Driver program to test above function
arr = [12, 13, 50, 10, 34, 1, 100]
print3largest(arr)

# Time Complexity: O(n)
# Space Complexity: O(1)