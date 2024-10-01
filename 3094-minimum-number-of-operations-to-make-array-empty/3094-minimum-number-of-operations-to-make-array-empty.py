class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        count=0
        for val in cnt.values():
            if val<2:
                return -1
            if val%3==0:
                count+=(val//3)
            else:
                count+=(val//3)+1
        return count
