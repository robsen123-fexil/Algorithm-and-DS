# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # arr=[]
        # temp=head
        # while temp:
        #     arr.append(temp.val)
        #     temp=temp.next
        # hsh={}
        # print(arr)
        # for i in arr:
        #     if i in hsh:
        #         hsh[i]+=1
        #     else:
        #         hsh[i]=1
        # result=[]
        # print(hsh)
        # for key , value in hsh.items():
        #     if value==1:
        #         result.append(key)
        # print(result)
        # dummy=ListNode(0)
        # tail=dummy
        # for i in result:
        #     tail.next=ListNode(i)
        #     tail=tail.next
        # return dummy.next
        if head==None:
            return head
        temp=head
        dummy=ListNode(0)
        tail=dummy
        prev=ListNode(None)
        # while temp and temp.next:
        #     if temp.val !=temp.next.val and temp.val!=prev:
        #         tail.next=ListNode(temp.val)
        #         tail=tail.next
        #     temp=temp.next
        #     prev=temp.val
        # return dummy.next
        while temp and temp.next:
            if prev!=temp.val and temp.val!=temp.next.val:
                tail.next=ListNode(temp.val)
                tail=tail.next
            prev=temp.val
            temp=temp.next
        if temp.val!=prev:
            tail.next=ListNode(temp.val)
            tail=tail.next
            
        return dummy.next
