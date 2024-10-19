class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        hsh=defaultdict(list)
        result=[]
        for i in range(len(nums)):
            if nums[i]==target:
                result.append(i)
        return [result[0] , result[-1]] if result else [-1 , -1]
