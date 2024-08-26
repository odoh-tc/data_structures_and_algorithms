#!/usr/bin/env python3

#Program to insert a new node in a linked list before a given node

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_before_node(head, key, data):

    if head is None:
        print("The linked list is empty.")
        return head
    
    new_node = Node(data)

    if head.data == key:
        new_node.next = head
        head = new_node
        return head
    

    current_node = head

    while current_node:
        if current_node.next.data == key:
            new_node.next = current_node.next
            current_node.next = new_node
            return head
        current_node = current_node.next

    print(f"The key {key} was not found in the linked list.")

    return head


# Test the function

def print_linked_list(head):
    current_node = head
    while current_node:
        print(current_node.data, end=" -> " if current_node.next else "\n")
        current_node = current_node.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print("Original linked list:")
print_linked_list(head)

new_data = 4
key = 2
head = insert_before_node(head, key, new_data)

print("\nLinked list after inserting a new node before", key, ":", new_data)
print_linked_list(head)


# Time complexity: O(n) as we need to traverse the linked list to find the given key.
# Space complexity: O(1) as we are using only a constant amount of extra space.


