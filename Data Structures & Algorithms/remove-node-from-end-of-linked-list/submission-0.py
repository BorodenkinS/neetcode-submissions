# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0

        curr = head
        while curr:
            curr = curr.next
            l -= 1

        if l + n == 0:
            return head.next
        
        curr = head
        while l + n < -1:
            l += 1
            curr = curr.next

        if not curr.next.next:
            curr.next = None
        else:
            curr.next = curr.next.next

        return head
            
        
        
