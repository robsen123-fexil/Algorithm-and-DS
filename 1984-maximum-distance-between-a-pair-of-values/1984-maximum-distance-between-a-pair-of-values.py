class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        l=r=0
        maxima=0
        while l<len(nums1) and r<len(nums2):
            if nums1[l]>nums2[r]:
                l+=1
            else:
                maxima=max(maxima , r-l)
                r+=1
        return maxima if maxima!=float('-inf') else 0