class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        stack1={}
        for i in nums:
            if i  in stack1:
                stack1[i]+=1
            else:

                stack1[i]=1
        return min(stack1 , key=stack1.get)
           

        