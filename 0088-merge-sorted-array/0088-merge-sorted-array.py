class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=m
        r=0
        while l<len(nums1) and r<n:
            nums1[l]=nums2[r]
            r+=1
            l+=1
        for i in range(len(nums1)):
            j=i
            while nums1[j]<nums1[j-1] and j>0:
                nums1[j] , nums1[j-1]=nums1[j-1] , nums1[j]
                j-=1
        
