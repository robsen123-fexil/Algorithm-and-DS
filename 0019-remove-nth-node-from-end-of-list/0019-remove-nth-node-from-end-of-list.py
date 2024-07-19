# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0 , head)
        lag=dummy
        lead=head
        while n>0 and lead:
            lead=lead.next
            n-=1
        while lead:
            lag=lag.next
            lead=lead.next
        lag.next=lag.next.next
        return dummy.next
