class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        count=0
        for i in nums1:
            i=pow(i , 2)
            hsh=defaultdict(int)
            for j in nums2:
                diff=i/j
                
                if diff in hsh:
                    print(diff)
                    count+=hsh[diff]
                hsh[j]+=1
        
        for i in nums2:
            i=pow(i , 2)
            hsh=defaultdict(int)
            for j in nums1:
                doff = i/j
                if doff in hsh:
                    count+=hsh[doff]
                hsh[j]+=1
        return count