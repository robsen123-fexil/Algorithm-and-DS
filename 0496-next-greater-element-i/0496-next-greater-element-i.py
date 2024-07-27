class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[-1]*len(nums1)
        stack=[]
        for ind , val in enumerate(nums2):
            while stack and stack[-1][1]<val:
                i , value =stack.pop()
                index=nums1.index(value)
                result[index]=val
            if val in nums1:
                stack.append([ind, val])
        print(result)
        return result                
        