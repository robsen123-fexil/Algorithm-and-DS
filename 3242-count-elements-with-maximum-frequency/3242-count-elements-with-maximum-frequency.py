class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        maxima=max(cnt , key=cnt.get)
        val=cnt[maxima]
        count=0
        for value in cnt.values():
            if value==val:
                count+=value
        return count