# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        def midPoint(head):
            slow = head
            fast = head

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
        
            return slow
        
        def reverse(head):
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

        def merge(head1, head2):
            head = head1
            counter = 1

            curr1 = head1.next
            curr2 = head2
            curr = head

            while curr2:
                if counter % 2 == 0:
                    temp = curr1
                    curr1 = curr1.next
                else:
                    temp = curr2
                    curr2 = curr2.next
                curr.next = temp
                curr = curr.next
                counter += 1

            if curr1:
                curr.next = curr1

        if head and head.next:
            mid = midPoint(head)
            half = mid.next
            mid.next = None
            half = reverse(half)
            merge(head, half)

