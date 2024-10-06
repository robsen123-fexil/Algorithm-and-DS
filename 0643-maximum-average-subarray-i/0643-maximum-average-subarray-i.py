class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res=nums[:k]
        l=0
        sums=sum(res)/k
        result=[]
        maxima=sums
        for i in range(k , len(nums)):
            sums*=k
            
            sums-=nums[l]
            l+=1
            sums+=nums[i]
            sums/=k
            maxima=max(maxima , sums)
        return maxima