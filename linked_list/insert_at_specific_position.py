#!/usr/bin/env python3

#program to insert the node at the specific position in the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def insert_at_position(head, position, data):
    if position <= 0:
        print("Position should be greater than 0.")
        return head

    new_node = Node(data)
    if position == 1:
        new_node.next = head
        head = new_node
        return head

    current_node = head
    for i in range(position - 2):
        if current_node is None:
            print("Position is out of bounds.")
            return head
        current_node = current_node.next

    if current_node is None or current_node.next is None:
        print("Position is out of bounds.")
        return head

    new_node.next = current_node.next
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
position = 3

head = insert_at_position(head, position, new_data)

print("\nLinked list after inserting a new node at position", position, ":", new_data)
current_node = head
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next


# Time complexity: O(n) as we need to traverse the linked list to find the previous node before inserting the new node.
# Space complexity: O(1) as we are using only a constant amount of extra space.