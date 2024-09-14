class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        result=[]
        MOD = 10**9 + 7
        for i in range(len(nums)):
            rev=int(str(nums[i])[::-1])
            result.append((nums[i]-rev))
        l=r=count=0
        hsh={}
        for diff in result:
            if diff in hsh:
                count = (count + hsh[diff]) % MOD
                hsh[diff]+=1
            else:
                hsh[diff]=1 
        
        return count