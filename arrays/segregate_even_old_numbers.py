#!/usr/bin/env python3

# def segregate_even_odd(arr, N):
#     even_nums = []
#     odd_nums = []

#     for i in range(N):
#         if arr[i] % 2 == 0:
#             even_nums.append(arr[i])
#         else:
#             odd_nums.append(arr[i])

#     # Combine even and odd numbers
#     ans = even_nums + odd_nums

#     for num in ans:
#         print(num, end=" ")

# # Driver Code
# arr = [7, 2, 9, 4, 6, 1, 3, 8, 5]
# N = len(arr)
# segregate_even_odd(arr, N)
# Time complexity = 0(n)
# Space complexity = 0(n)


def segregate_even_odd(arr, N):

    i = -1
    j = 0


    while j < N:
        if arr[j] % 2 == 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    for num in arr:
        print(num, end=" ")


# Driver Code
arr = [7, 2, 9, 4, 6, 1, 3, 8, 5]
N = len(arr)
segregate_even_odd(arr, N)
# Time complexity = 0(n)
# Space complexity = 0(1)