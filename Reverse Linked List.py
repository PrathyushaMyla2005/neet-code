'''2️⃣ Why we reverse a linked list?

Reversing a linked list is a common operation in many problems like:

Palindrome check in linked list

Reversing data order for processing

Stack implementation using linked list
Input: 1 -> 2 -> 3 -> 4 -> 5 -> None
Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
'''
'''3️⃣ Approaches
Approach 1: Iterative (Most Common)

Idea:

Use three pointers: prev, curr, next.

Traverse the list and reverse the next pointer of each node.

Steps:

Initialize prev = None and curr = head.

Loop while curr != None:

Store next = curr.next

Point curr.next = prev

Move prev = curr and curr = next

Finally, prev will be the new head.
Time Complexity: O(n) → Traverse all n nodes once
Space Complexity: O(1) → Only 3 extra pointers used'''
# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to reverse linked list
def reverseLinkedList(head):
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next    # store next node
        curr.next = prev         # reverse pointer
        prev = curr              # move prev forward
        curr = next_node         # move curr forward
    return prev  # new head

# Function to print linked list
def printLinkedList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

# Create linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original Linked List:")
printLinkedList(head)

# Reverse linked list
reversed_head = reverseLinkedList(head)

print("Reversed Linked List:")
printLinkedList(reversed_head)
'''Approach 2: Recursive Method

Instead of using a loop, we can reverse the linked list recursively.

Idea

Go to the end of the list using recursion.

Reverse the pointers while returning from the recursive call.'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLinkedListRecursive(head):
    # Base case: empty list or single node
    if head is None or head.next is None:
        return head
    
    # Recursively reverse the rest of the list
    new_head = reverseLinkedListRecursive(head.next)
    
    # head.next is the last node of reversed part
    head.next.next = head  # reverse pointer
    head.next = None       # make current node point to None
    
    return new_head  # new head of reversed list

# Helper function to print linked list
def printLinkedList(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

# Example
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original Linked List:")
printLinkedList(head)

reversed_head = reverseLinkedListRecursive(head)
print("Reversed Linked List (Recursive):")
printLinkedList(reversed_head)
