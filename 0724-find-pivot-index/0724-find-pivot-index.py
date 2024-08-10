class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        right=sum(nums[1:])
        
        for i in range(1, len(nums)):
            if left==right:
                return i-1
            print(right , left)
            
            left+=nums[i-1]
            right-=nums[i]
        print(left , right)
        if left==right:
            return len(nums)-1
        else:
            return -1

        