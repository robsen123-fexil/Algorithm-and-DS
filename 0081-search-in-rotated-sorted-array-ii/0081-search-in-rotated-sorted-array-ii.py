class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # return True if target in nums else  False
        l =0
        r=len(nums)-1
        while l <=r :
            mid = l + (r-l) // 2
            if nums[mid] == target:
                return True 
            if nums[mid] > nums[l]:
                if nums[mid] > target >= nums[l]:
                    r=mid-1
                else:
                    l=mid+1
        
            elif nums[mid] < nums[l]:
                if nums[mid] < target <=nums[r]:
                    l=mid+1
                else:
                    r=mid-1

            else:
                l+=1
        return False
