class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # l=r=k=0
        # for i in range(len(nums2)):
        #     nums1[m+i]=nums2[i]
        # print(nums1)
        # while l<m and r<n:
        #     if nums1[l]<=nums2[r]:
        #         nums1[k]=nums1[l]
        #         l+=1
        #     else:
        #         nums1[k]=nums2[r]
        #         r+=1
        #     k+=1
        # while l<m:
        #     nums1[k]=nums1[l]
        #     l+=1
        #     k+=1
        # while r<n:
        #     nums1[k]=nums2[r]
        #     r+=1
        #     k+=1
        for i in range(len(nums2)):
            nums1[m+i]=nums2[i]
        for i in range(1 , len(nums1)):
            j=i
            while nums1[j-1] >=nums1[j] and j>0:
                nums1[j-1] , nums1[j]=nums1[j] , nums1[j-1]
                j-=1
        
        

        