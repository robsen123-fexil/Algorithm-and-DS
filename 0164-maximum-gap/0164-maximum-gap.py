class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maximal=[float("-inf")]
        x=0
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                x=nums[j]-nums[i]
                maximal.append(x)
                break
        return max(maximal) if len(nums)>=2 else 0
                
                
        