class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # l=0
        mid=0
        num=nums1+nums2

        # r=len(num)-1
        num.sort()
        # mid=float(num[l]+num[r])/2
        # return mid
        if len(num)%2==0:
            md=len(num)//2
            res=num[:md]
            ras=num[md:]
            mid=(res[-1]+ras[0])/2
            return mid
        else:
            return float(num[len(num) // 2])
            
            


        
        