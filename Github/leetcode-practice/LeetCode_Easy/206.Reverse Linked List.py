# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            new= curr.next #save the curr. next location
            curr.next = prev # reverse the node 
            prev = curr # what is the location of prev
            curr = new # what is curr location 
        return prev 



