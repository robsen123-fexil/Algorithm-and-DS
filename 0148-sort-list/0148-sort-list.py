# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        current=head
        while current:
            res.append(current.val)
            current=current.next
        res.sort()
        dummy=ListNode(0)
        current=dummy
        for i in res:
            current.next=ListNode(i)
            current=current.next
        return dummy.next
