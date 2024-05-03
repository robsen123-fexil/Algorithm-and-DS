class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        place=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[place]=nums[i]
                place+=1
        return place
        