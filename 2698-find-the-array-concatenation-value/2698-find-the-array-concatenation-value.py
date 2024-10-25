class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        strs=0
        res=[]
        while l<=r:
            if l!=r:
               res.append(str(nums[l])+str(nums[r]))
               r-=1
               l+=1
            else:
                res.append(str(nums[r]))
                break
        val=0
        for i in range(len(res)):
            val+=int(res[i])
        return val
