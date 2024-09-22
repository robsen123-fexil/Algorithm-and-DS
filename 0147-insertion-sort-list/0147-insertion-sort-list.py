# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        temp=head
        while temp:
            res.append(temp.val)
            temp=temp.next
        for i in range(1 , len(res)):
            j=i
            while res[j-1]>=res[j] and j>0:
                res[j] , res[j-1]=res[j-1] , res[j]
                j-=1
        dummy=ListNode(0)
        tail=dummy
        for i in res:
            tail.next=ListNode(i)
            tail=tail.next
        return dummy.next
        