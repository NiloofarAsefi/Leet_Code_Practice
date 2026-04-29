# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next: # fast is not None and fast.next is not None
            slow = slow.next
            fast = fast.next.next # fast moves 2 steps, slow moves 1 step.
        return slow 
    
        # slow is the midele node which is connected to the end of list. 
        # fast is the end of list.
        # when fast is at the end of list, slow is at the middle of list.
