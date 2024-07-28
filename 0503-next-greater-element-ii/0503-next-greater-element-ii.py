class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        result=[-1]*len(nums)
        for ind , val in enumerate(nums):
            while stack and stack[-1][1] < val:
                index , value =stack.pop()
                result[index]=val
            stack.append([ind , val])
        print(result)
        print(stack)
        for i  , val in enumerate(nums):
            while stack and stack[-1][1]<val:
                index , value = stack.pop()
                result[index]=val
                
        print(result)
        return result     