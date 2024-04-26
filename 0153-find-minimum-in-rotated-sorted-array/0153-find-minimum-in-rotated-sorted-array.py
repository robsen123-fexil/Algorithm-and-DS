class Solution:
    def findMin(self, nums: List[int]) -> int:
        lists=[]
        x=nums.index(min(nums))
        d=x-1
        for i in range(len(nums)-d, len(nums)):
            lists.append(nums[i])
        for i in range(0 , len(lists)-d):
            lists.append(list[i])
        l=0
        r=len(nums)-1
        while l<=r:
            mid = (l+r) // 2
            if nums[mid] < nums[r]:
                r=mid
            else:
                l=mid+1
        return nums[mid]
    
            

