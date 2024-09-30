class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count=0
        res=set()
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if abs(nums[i]-nums[j])==k:
                    print(nums[i] , nums[j])
                    res.add((nums[i] , nums[j]))
                    count+=1
        resu=[]
        print(res)
        for i in res:
            print(i)
            r=sorted(list(i))
            if r not in resu:
                resu.append(r)
        return len(resu)