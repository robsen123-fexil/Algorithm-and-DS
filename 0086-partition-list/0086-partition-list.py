# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        res=[]
        current=head
        while current:
            res.append(current.val)
            current=current.next
        first=[]
        sec=[]
        for i in range(len(res)):
            if res[i]<x:
                first.append(res[i])
            else:
                sec.append(res[i])
        ans=first+sec
        dummy=ListNode(0)
        current=dummy
        for i in ans:
            current.next=ListNode(i)
            current=current.next
        return dummy.next