class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        cnt=Counter(nums)
        for val in cnt.values():
            if val%3==0:
                count+=(val//3)
                
            elif val==1:
                return -1
            else:
                count+=(val//3)+1
        return count