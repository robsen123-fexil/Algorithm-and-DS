class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        hsh={}
        res=[-1]*len(nums1)
        for i , val in enumerate(nums1):
            hsh[val]=i
        for i in range(len(nums2)):
            while stack and nums2[i]>stack[-1]:
                ind=hsh[stack.pop()]
                res[ind]=nums2[i]
            if nums2[i] in nums1:
                stack.append(nums2[i])
        return res
