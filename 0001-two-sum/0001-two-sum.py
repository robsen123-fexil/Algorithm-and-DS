class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap={}
        # for i , n in enumerate(nums):
        #     differnce=target-n
        #     if differnce in hashmap:
        #         return [hashmap[differnce], i]
        #     hashmap[n]=i
        # return hashmap
        hsh={}
        for i , value in enumerate(nums):
            df=target-value
            if df in hsh:
                return [hsh[df] , i]
            hsh[value] = i
        