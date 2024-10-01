class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt=Counter(nums)
        v=len(nums)//2
        leng=0
        for val in cnt.values():
            if val%2==0:
                leng+=(val//2)
        return leng==v
