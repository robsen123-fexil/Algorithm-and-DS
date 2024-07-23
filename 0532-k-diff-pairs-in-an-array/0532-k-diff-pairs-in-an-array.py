class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count=0
        result=[]
        for i in range(len(nums)):
            for j in range(i+1  , len(nums)):
                val=abs(nums[i] -nums[j])
                if val==k:
                    res=[nums[i] , nums[j]]
                    res.sort()
                    if  res not in result:
                       result.append(res)
        print(result)
        return len(result)
        