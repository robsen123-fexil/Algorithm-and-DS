# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp=head
        dummy1=ListNode(0)
        tail1=dummy1
        dummy2=ListNode()
        tail2=dummy2
        while temp:
            if temp.val<x:
                tail1.next=ListNode(temp.val)
                tail1=tail1.next
            else:
                tail2.next=ListNode(temp.val)
                tail2=tail2.next
            temp=temp.next
        print(dummy2)
        temp2=dummy2.next
        while temp2:
            tail1.next=ListNode(temp2.val)
            tail1=tail1.next
            temp2=temp2.next

        return dummy1.next
        
        