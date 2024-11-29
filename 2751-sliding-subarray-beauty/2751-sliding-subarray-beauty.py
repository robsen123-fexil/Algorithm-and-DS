class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        ans, sort_list = [], []
        for i, n in enumerate(nums):
            if n < 0:
                bisect.insort(sort_list, n)
            if i >= k and nums[i-k] < 0:
                del sort_list[bisect.bisect_left(sort_list, nums[i-k])]
            if i >= k-1:
                ans.append(sort_list[x-1] if len(sort_list) >= x else 0)
        return ans     