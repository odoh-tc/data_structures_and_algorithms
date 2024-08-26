#!/usr/bin/env python3

# Program to reverse a linked list by using a stack

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_by_stack(head):
    stack = []

    current_node = head

    # Push all nodes onto the stack
    while current_node is not None:
        stack.append(current_node)
        current_node = current_node.next

    # Set the new head to the last node
    head = stack.pop()
    current_node = head

    # Pop nodes from the stack and fix the next pointers
    while stack:
        current_node.next = stack.pop()
        current_node = current_node.next

    # The last node should point to None
    current_node.next = None
    return head

# Test the function

def print_linked_list(head):
    current_node = head
    while current_node:
        print(current_node.data, end=" -> " if current_node.next else "\n")
        current_node = current_node.next

# Creating a linked list 1 -> 2 -> 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print("Original linked list:")
print_linked_list(head)

reversed_head = reverse_by_stack(head)

print("Reversed linked list:")
print_linked_list(reversed_head)
