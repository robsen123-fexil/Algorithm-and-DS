class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        cnt = Counter(nums[:k])
        sums = sum(nums[:k])
        maxima = float("-inf")
        if len(cnt) >= m:
            maxima = max(maxima, sums)
        l = 0
        for i in range(k, len(nums)):
            cnt[nums[l]] -= 1
            cnt[nums[i]] += 1
            sums -= nums[l]
            sums += nums[i]
            if cnt[nums[l]] == 0:
                cnt.pop(nums[l])
            if len(cnt) >= m:
                maxima = max(maxima, sums)
            l += 1
        return maxima if maxima != float("-inf") else 0
