'''1️⃣ Question Explanation

You are given two sorted linked lists, l1 and l2.
Your task: merge them into a single sorted linked list and return the head of the merged list.

Example:

Input: l1 = 1 -> 2 -> 4
       l2 = 1 -> 3 -> 4
Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
Important points:

Both lists are already sorted in ascending order.

You need to maintain the sorted order in the merged list.

You can return either a new list or merge in-place.'''
'''Approach 1: Iterative Merge (Preferred)

We use a dummy node to simplify the merging.

Steps:

Create a dummy node that will point to the head of the merged list.

Maintain a pointer current that tracks where to attach the next node.

Compare the first nodes of l1 and l2.

Attach the smaller node to current.next.

Move the pointer of the list from which you took the node.

Move current forward.

After one list ends, attach the remaining nodes of the other list.

Return dummy.next as the head of the merged list.'''
# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Merge two sorted linked lists
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Attach remaining nodes
        if l1:
            current.next = l1
        if l2:
            current.next = l2

        return dummy.next

# Helper: convert Python list to linked list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper: print linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(" -> ".join(map(str, result)))

# Example input lists
l1 = create_linked_list([1, 3, 5])
l2 = create_linked_list([2, 4, 6])

# Merge lists
solution = Solution()
merged_head = solution.mergeTwoLists(l1, l2)

# Print merged linked list
print_linked_list(merged_head)
'''Why we use the recursive approach

Simplicity and elegance:

The recursive solution is very clean—less code than iterative.

Each call handles merging the first node of the lists and delegates the rest to recursion.

Conceptually easy:

It naturally follows the definition of a merged sorted list:

“The first node of the merged list is the smaller of the first nodes of the two lists, and the rest is the merge of the remaining nodes.”

Good for functional thinking:

No explicit dummy node or iteration is needed.

Just smaller node → recursive merge → attach next.
Time Complexity (T.C)

Every node from l1 and l2 is visited exactly once.

So if n is the length of l1 and m is the length of l2:

T.C
=
𝑂
(
𝑛
+
𝑚
)
T.C=O(n+m)
Space Complexity (S.C)
S.C=O(n+m)
'''
# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Recursive merge
class Solution:
    def mergeTwoLists(self, l1, l2):
        # Base cases
        if not l1:
            return l2
        if not l2:
            return l1
        
        # Recursive case
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# Helper: convert Python list to linked list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper: print linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(" -> ".join(map(str, result)))

# Example input lists
l1 = create_linked_list([1, 3, 5])
l2 = create_linked_list([2, 4, 6])

# Merge lists recursively
solution = Solution()
merged_head = solution.mergeTwoLists(l1, l2)

# Print merged linked list
print_linked_list(merged_head)
