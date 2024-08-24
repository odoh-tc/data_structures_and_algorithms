#!/usr/bin/env python3

#python program to insert a new node after a given node in the linked list

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None




# def insertAfter(prev_node, new_data):
#     if prev_node is None:
#         print("The given previous node must be in the linked list")
#         return

#     new_node = Node(new_data)
#     new_node.next = prev_node.next
#     prev_node.next = new_node
#     return new_node


# # Test the function
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)

# print("Original linked list:")
# current_node = head
# while current_node:
#     print(current_node.data, end=" ")
#     current_node = current_node.next


# new_data = 4
# prev_node = head.next

# new_node = insertAfter(prev_node, new_data)

# print("\nLinked list after inserting a new node after", prev_node.data, ":", new_data)
# current_node = head
# while current_node:
#     print(current_node.data, end=" ")
#     current_node = current_node.next


# # Time complexity: O(1) as we are inserting the new node after the given previous node, regardless of the size of the linked list.
# # Space complexity: O(1) as we are using only a constant amount of extra space.



def insertAfter(head, key, new_data):
    if head is None:
        print("The linked list is empty.")
        return head

    new_node = Node(new_data)
    current_node = head

    while current_node:
        if current_node.data == key:
            new_node.next = current_node.next
            current_node.next = new_node
            print(f"Inserted node with data {new_data} after node with data {key}.")
            return head
        current_node = current_node.next

    print(f"The key {key} was not found in the linked list.")
    return head





# Test the function
head = Node(1)
second = Node(2)
third = Node(3)

# Linking nodes
head.next = second
second.next = third

# Function to print linked list
def printLinkedList(node):
    current = node
    while current:
        print(current.data, end=" -> " if current.next else "\n")
        current = current.next

print("Original linked list:")
printLinkedList(head)



new_data = 4
key = 1

head = insertAfter(head, key, new_data)

print("\nLinked list after inserting a new node after", key, ":", new_data)
printLinkedList(head)


# Time complexity: O(n) as we need to traverse the linked list to find the given key.
# Space complexity: O(1) as we are using only a constant amount of extra space.