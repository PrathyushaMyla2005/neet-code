'''📌 Question Understanding

You are given two sorted linked lists (in non-decreasing order).
You need to merge them into a single sorted linked list and return its head.

👉 Example:

list1 = 1 -> 2 -> 4

list2 = 1 -> 3 -> 4
✅ Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4'''
'''Approaches
🔹 Approach 1: Iterative (Optimal)

Use a dummy node to simplify merging.

Have a pointer tail that always points to the last node in the new merged list.

Compare the current nodes of both lists:

Attach the smaller node to tail.

Move that list’s pointer forward.

Continue until one list becomes NULL.

Attach the remaining nodes from the non-empty list.

Return dummy.next (skipping dummy node).

✅ Example trace with list1 = 1->2->4 and list2 = 1->3->4:

Compare 1 & 1 → attach 1 (from list1).

Compare 2 & 1 → attach 1 (from list2).

Compare 2 & 3 → attach 2 (from list1).

Compare 4 & 3 → attach 3 (from list2).

Compare 4 & 4 → attach 4 (from list1).

Attach remaining 4 (from list2).

Result: 1 -> 1 -> 2 -> 3 -> 4 -> 4
⇒ T.C = O(m + n)
S.C = O(1) (constant extra space).'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # Step 1: Create a dummy node (acts like a placeholder head)
    dummy = ListNode(-1)
    tail = dummy  # tail points to the end of merged list

    # Step 2: Compare both lists until one becomes empty
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1  # attach list1 node
            list1 = list1.next # move list1 forward
        else:
            tail.next = list2  # attach list2 node
            list2 = list2.next # move list2 forward
        tail = tail.next      # move tail forward

    # Step 3: Attach the remaining nodes
    if list1:
        tail.next = list1
    else:
        tail.next = list2

    # Step 4: Return merged list (skip dummy)
    return dummy.next

# Helper function to print linked list
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# ✅ Correct way to create linked lists:
# list1 = 1 -> 2 -> 4
list1 = ListNode(1, ListNode(2, ListNode(4)))

# list2 = 1 -> 3 -> 4
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Merge lists
merged = mergeTwoLists(list1, list2)

# Print result
printList(merged)
'''T.C.=O(m+n)
S.C.=O(m+n)
'''
#recurvise
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # Base cases
    if not list1:  # if list1 is empty, return list2
        return list2
    if not list2:  # if list2 is empty, return list1
        return list1

    # Recursive case: choose smaller node
    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)  # attach rest
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)  # attach rest
        return list2

# Helper function to print linked list
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# ✅ Create linked lists:
# list1 = 1 -> 2 -> 4
list1 = ListNode(1, ListNode(2, ListNode(4)))

# list2 = 1 -> 3 -> 4
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Merge using recursion
merged = mergeTwoLists(list1, list2)

# Print result
printList(merged)
