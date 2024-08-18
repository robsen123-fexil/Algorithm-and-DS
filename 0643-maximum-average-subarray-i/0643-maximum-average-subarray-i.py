class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxima=sum(nums[:k])/k
        sums=sum(nums[:k])
        l=0
        for i in range(k , len(nums)):
            sums+=nums[i]
            sums-=nums[l]
            maxima=max(maxima , sums/k )
            l+=1
        return maxima
            
