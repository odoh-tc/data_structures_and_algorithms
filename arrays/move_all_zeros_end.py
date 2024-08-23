#!/usr/bin/env python3


A = [5, 6, 0, 4, 6, 0, 9, 0, 8]
n = len(A)
B = [0] * n
j = 0
count = 0

for i in range(n):
    if A[i] != 0:
        B[j] = A[i]
        j += 1
    else:
        count += 1

while count > 0:
    B[j] = 0
    j += 1
    count -= 1



for i in range(n):
    A[i] = B[i]

for i in range(n):
    print(A[i], end=" ")

print() 

    

# Time complexity: O(n), where n is the size of elements of the input array.
# Auxiliary Space : O(n), as we are using an extra array to store the elements of the input array.