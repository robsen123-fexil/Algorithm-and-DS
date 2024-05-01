class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums1:
            if i in nums2:
                res.append(i)
                del nums2[nums2.index(i)]
        return res


       
