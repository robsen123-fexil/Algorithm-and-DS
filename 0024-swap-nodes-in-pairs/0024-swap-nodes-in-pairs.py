# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head.next==None:
        #     return 
        # slow=head
        # fast=head.next
        # while fast.next.next:
        #     nxt=fast.next
        #     slow.next=nxt
        #     fast.next=slow
        #     fast=fast.next.next
        #     slow=slow.next.next
        # return head
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        for i in range(1 , len(arr) , 2):
            arr[i] , arr[i-1] = arr[i-1] , arr[i]

        
        
        
        print(arr)
        dummy=ListNode(0)
        tail=dummy
        for i in arr:
            tail.next=ListNode(i)
            tail=tail.next
        return dummy.next

        