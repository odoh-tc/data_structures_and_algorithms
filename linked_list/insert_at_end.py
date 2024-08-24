#!/usr/bin/env python3

#python program to insert a node at the end of the linked list


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_end(head, new_data):
    new_node = Node(new_data)
    if head is None:
        head = new_node
        return head

    current_node = head
    while current_node.next:
        current_node = current_node.next

    current_node.next = new_node
    return head


# Test the function
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print("Original linked list:")
current_node = head
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next



new_data = 4
head = insert_at_end(head, new_data)

print("\nLinked list after inserting a new node at the end:", new_data)
current_node = head
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next


# Time complexity: O(n) as we need to traverse the linked list to find the last node before inserting the new node.
# Space complexity: O(1) as we are using only a constant amount of extra space.