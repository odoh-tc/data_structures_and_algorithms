#!/usr/bin/env python3

#program to find the total length of a linked list

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


def length_linked_list(head):

    if head == None:
        print("/nThe linked list is empty.")
        return 0
    
    count = 0
    current_node = head
    while current_node:
        count += 1
        current_node = current_node.next

    print(f"\nThe total length of the linked list is {count}.")
    return count


# Test the function

head = Node(1)
head.next = Node(5)
head.next.next = Node(7)

length_linked_list(head)

# Time complexity: O(n) as we need to traverse the linked list once to count the nodes.
# Space complexity: O(1) as we are using only a constant amount of extra space.

