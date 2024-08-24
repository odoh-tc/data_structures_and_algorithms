#!/usr/bin/env python3
# Python Program to insert the node at the beginning of the linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    


def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head


# Test the function
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(5)

print("Original linked list:")
current_node = head
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next


new_data = 4
head = insert_at_beginning(head, new_data)

print("\nLinked list after inserting at the beginning:", new_data)
current_node = head
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next


# Time complexity: O(1) as we are inserting the node at the beginning of the linked list.
# Space complexity: O(1) as we are using only a constant amount of extra space.