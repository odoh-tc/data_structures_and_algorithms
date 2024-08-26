#!/usr/bin/env python3

#program to search an element in a linked list with the position of the element

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


def search_element(head, key):
    if head is None:
        print("\nLinked list is empty.")
        return False
    
    if head == key:
        print(f"\n{key} found at position 1.")
        return True
    
    current_node = head
    position = 1
    while current_node:
        if current_node.data == key:
            print(f"\n{key} found at position {position}.")
            return True
        current_node = current_node.next
        position += 1

    print(f"\n{key} not found in the linked list.")

    return False


# Test the function

def print_linked_list(head):
    current_node = head
    while current_node:
        print(current_node.data, end=" -> " if current_node.next else "\n")
        current_node = current_node.next


head = Node(1)
head.next = Node(5)
head.next.next = Node(7)

print("Original linked list:")
print_linked_list(head)

key = 9
search_element(head, key)
