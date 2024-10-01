class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt=Counter(nums)
        count=res=0
        for val in cnt.values():
            if val%2==0:
                count+=(val//2)
            else:
                res+=1
                count+=(val//2)
        return [count , res]