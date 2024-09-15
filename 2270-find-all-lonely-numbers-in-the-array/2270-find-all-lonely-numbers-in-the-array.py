class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        cnt=Counter(nums)
        result=[]
        for key , value in cnt.items():
            if value == 1 and (key-1) not in cnt and (key+1) not in cnt:
                result.append(key)
        return result