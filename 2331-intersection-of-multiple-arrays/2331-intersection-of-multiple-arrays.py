class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hsh=defaultdict(int)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                hsh[nums[i][j]]+=1
        res=[]
        for key , val in hsh.items():
            if val ==len(nums):
                res.append(key)
        print(res)
        return sorted(res)
            