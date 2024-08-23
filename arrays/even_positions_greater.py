#!/usr/bin/env python3

def even_positions_are_greater(arr, N):

    arr.sort()
    ans = [0] * N
    ptr1 = 0
    ptr2 = N -1


    for i in range(N):
        #check for even positions
        if i % 2 == 0:
            ans[i] = arr[ptr2]
            ptr2 -= 1

        #check for odd positions

        else:
            ans[i] = arr[ptr1]
            ptr1 += 1


    for i in range(N):
        print(ans[i], end = " ")



# Driver Code
arr = [1, 2, 1, 2]
N = len(arr)
even_positions_are_greater(arr, N)


# Time Complexity: O(NlogN)
# spce Complexity: O(N)
