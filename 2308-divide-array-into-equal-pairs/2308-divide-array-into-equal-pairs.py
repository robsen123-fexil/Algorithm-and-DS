class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        l=0
        r=1
        result=[]
        while r<(len(nums)):
            result.append(nums[l:r+1])
            r+=2
            l+=2
        
        for i in result:
            cnt=Counter(i)
            if len(cnt)!=1:
                return False

        return 1