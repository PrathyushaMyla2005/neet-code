'''You are given the head of a linked list. Determine whether the linked list contains a cycle.

A cycle means that if we keep following the next pointers, at some point, we’ll revisit a previously visited node → i.e., it loops forever instead of ending with None.

Example 1 (Cycle exists):
1 → 2 → 3 → 4
        ↑    |
        |____|


Here, node 4 points back to node 2, so it loops forever → Cycle exists ✅'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    visited = set()
    current = head
    while current:
        if current in visited:  # already visited → cycle
            return True
        visited.add(current)
        current = current.next
    return False
'''Time Complexity: O(n) → each node visited once

Space Complexity: O(n) → storing visited nodes'''
def hasCycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next         # move 1 step
        fast = fast.next.next    # move 2 steps
        if slow == fast:         # pointers meet → cycle
            return True
    return False
'''Time Complexity: O(n)

Worst case: traverses whole list once.

Space Complexity: O(1)

Only two pointers used.

🔹 Why use Floyd’s Algorithm instead of Hashing?

Hashing uses extra memory → O(n)

Floyd’s is memory efficient → O(1)

For interview / placement, Floyd’s Cycle Detection is preferred ✅

🔹 Final Summary

Problem: Detect if a linked list has a cycle.

Approaches:

Hashing (O(n) time, O(n) space) → easy

Floyd’s Cycle Detection (O(n) time, O(1) space) → optimal

Always mention both approaches in interview → then say Floyd’s is optimal.

Do you want me to also show you a step-by-step trace example (like dry run) of Floyd’s algorithm with a small list? That will make the "meeting point" idea super clear.'''