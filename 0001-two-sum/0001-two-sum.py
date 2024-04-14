class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i , n in enumerate(nums):
            differnce=target-n
            if differnce in hashmap:
                return [hashmap[differnce], i]
            hashmap[n]=i
        return hashmap

        