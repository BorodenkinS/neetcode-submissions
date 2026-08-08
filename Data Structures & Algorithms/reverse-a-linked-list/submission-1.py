# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        curr_head = head
        curr = head.next

        while curr:
            temp = curr_head
            curr_head = curr
            curr = curr.next
            curr_head.next = temp
            head.next = curr
            
        return curr_head


