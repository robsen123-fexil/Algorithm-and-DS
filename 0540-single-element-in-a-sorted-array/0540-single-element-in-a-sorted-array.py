class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        mini=min(cnt.values())
        for key , val in cnt.items():
            if mini==val:
                return key