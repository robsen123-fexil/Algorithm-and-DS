class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        result=[-1]*len(nums)
        for i in range(len(nums)):
            if stack :
                while stack and stack[-1][0]<nums[i]:
                    a , b = stack.pop()
                    result[b]=nums[i]
                stack.append([nums[i] , i])
            else:
                stack.append([nums[i] , i ])
        print(result , stack)
        for i , val in enumerate(nums):
            while stack and stack[-1][0]<val:
                a , b =stack.pop()
                result[b]=val
        return result
