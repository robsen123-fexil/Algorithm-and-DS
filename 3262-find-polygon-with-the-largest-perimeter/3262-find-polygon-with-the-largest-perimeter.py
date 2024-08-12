class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sums=sum(nums)
        nums.sort(reverse=True)
        for i in range(len(nums)):
            sums-=nums[i]
            if sums<=nums[i]:
                continue
            else:
                return sums+nums[i]
        return -1

            

