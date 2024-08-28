#!/usr/bin/env python3

#program to delete a node from the beginning of a linked list


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_from_beginning(head):
    if head is None:
        print("The linked list is empty.")
        return head
    
    new_head = head.next
    del head
    return new_head

# Test the function


# Create a sample linked list
head = Node(1)
second = Node(2)
third = Node(3)

head.next = second
second.next = third

print("Original linked list:")
current_node = head
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next


# Delete the first node
head = delete_from_beginning(head)

print("\nLinked list after deleting the first node:")
current_node = head
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next

# Time complexity: O(1) as we are deleting the first node of the linked list.
# Space complexity: O(1) as we are using only a constant amount of extra space.