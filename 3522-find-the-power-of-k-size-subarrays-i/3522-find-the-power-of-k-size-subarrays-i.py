class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def consec(res):
            for i in range(1  , len(res)):
                if res[i]-res[i-1]!=1:
                    return False
            return True

        res=nums[:k]
        result=[]
        if res==sorted(res) and consec(sorted(res)):
            result.append(max(res))
        else:
            result.append(-1)
        l=0
        for i in range(k , len(nums)):
            res.append(nums[i])
            res.remove(nums[l])
            l+=1
            if res==sorted(res) and consec(sorted(res)):
                result.append(max(res))
            else:
                result.append(-1)
        return result