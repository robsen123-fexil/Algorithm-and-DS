class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        r=nums[len(nums)-1]
        ans=[]
        for i in range(len(nums)):
            ans.append(i)
            i+=1

        ans.append(len(nums))
        for i in range(len(ans)):
            if ans[i] not in nums:
                return ans[i]
            