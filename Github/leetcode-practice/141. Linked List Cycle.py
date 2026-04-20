# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next: 
            slow =slow.next
            fast = fast.next.next
            if slow == fast:
                return True   
        return False

# Time Complexity: O(n)  
# Space: O(1): You only use two pointers: slow and fast.
# No extra data structure is used.

