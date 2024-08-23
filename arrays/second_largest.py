#!/usr/bin/env python3

# def second_largest(arr):

#     arr_size = len(arr)

#     if arr_size < 2:
#         print("Invalid Input")
#         return
    
#     first = second = float('-inf')

#     for i in range(arr_size):
#         if arr[i] > first:
#             second = first
#             first = arr[i]
#         elif arr[i] > second and arr[i] != first:
#             second = arr[i]

#     print("Second largest element is", second)


# # Driver program to test above function
# arr = [12, 13, 10, 34, 100, 100]
# second_largest(arr)

def second_largest(arr, arr_size):

    arr.sort(reverse=True)

    for i in range(1, arr_size):
        if (arr[i] != arr[0]):
            print("The second largest element is", arr[i])
            break

    if (arr[0] == arr[1]):
        print("No second largest element found")

    print(arr)
    print(arr_size)


arr = [500, 13, 150, 34, 100, 100]
arr_size = len(arr)
second_largest(arr, arr_size)




# Time Complexity: O(nlogn), where n is the size of input array.
# Auxiliary space: O(1), as no extra space is required.