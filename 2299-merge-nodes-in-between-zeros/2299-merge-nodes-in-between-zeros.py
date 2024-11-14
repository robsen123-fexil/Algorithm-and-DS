# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lists=[]
        node=head
        while node:
            lists.append(node.val)
            node=node.next
        l=0
        r=1
        res=[]
        while r<len(lists)-1:
            sums=0
            while lists[r]!=0:
                r+=1
            while l<r:
                sums+=lists[l]
                l+=1
            r+=1
            res.append(sums)
        dummy=ListNode(0)
        heads=dummy
        for i in res:
            heads.next=ListNode(i)
            heads=heads.next
        return dummy.next
        


        
