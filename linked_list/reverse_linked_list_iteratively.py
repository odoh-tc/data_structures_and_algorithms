#!/usr/bin/env python3

#program to reverse a linked list using iterative approach


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head):
    if head is None:
        print("The linked list is empty.")
        return head
    
    prev_node = None
    current_node = head

    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    head = prev_node

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

reversed_head = reverse_list(head)

print("Reversed linked list:")
print_linked_list(reversed_head)

# Time complexity: O(n) as we need to traverse the linked list once.
# Space complexity: O(1) as we are using only a constant amount of extra space.