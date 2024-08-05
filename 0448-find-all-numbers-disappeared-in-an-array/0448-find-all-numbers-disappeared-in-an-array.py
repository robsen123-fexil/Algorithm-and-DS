class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hsh={}
        for i in range(1, len(nums)+1):
            hsh[i]=0
        for i in nums:
            hsh[i]+=1
        solution=[]
        for key , value in hsh.items():
            if value==0:
                solution.append(key)
        return solution        