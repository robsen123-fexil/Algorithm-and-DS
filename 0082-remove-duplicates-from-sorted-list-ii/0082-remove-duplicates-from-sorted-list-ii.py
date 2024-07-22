# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        hsh={}
        print(arr)
        for i in arr:
            if i in hsh:
                hsh[i]+=1
            else:
                hsh[i]=1
        result=[]
        print(hsh)
        for key , value in hsh.items():
            if value==1:
                result.append(key)
        print(result)
        dummy=ListNode(0)
        tail=dummy
        for i in result:
            tail.next=ListNode(i)
            tail=tail.next
        return dummy.next