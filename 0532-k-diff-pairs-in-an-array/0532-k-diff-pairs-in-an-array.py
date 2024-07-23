class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        l=0
        r=len(nums)-1
        count=0
        nums.sort()
        while l<len(nums)-1:
            while l<r:
                val=abs(nums[l]-nums[r])
                if val==k:
                    count+=1
                    break
                r-=1   
            while l<(len(nums)-1):
                if nums[l+1] !=nums[l]:
                    l+=1
                    break
                l+=1
            r=len(nums)-1
        return count
            

            



        