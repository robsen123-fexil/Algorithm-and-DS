class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res=[]
        mod=(10**(9))+7
        for i in range(len(nums)):
            sums=nums[i]
            res.append(sums)
            for j in range(i+1 , len(nums)):
                sums+=nums[j]
                res.append(sums)
        res.sort()
        print(res)
        su=0
        for i in range(left-1 , right):
            print(i)
            su+=res[i]
        return su%(mod)