class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        res={}
        for key , val in cnt.items():
            if key%2==0:
                res[key]=val
        print(res)
        maxima=float('-inf')
        if res:
           maxima=max(res , key=res.get)
        else:
            return -1
        vall=res[maxima]
        resu=[]
        for key , val in res.items():
            if val==vall:
                resu.append(key)
        print(maxima)
        return min(resu) if resu else -1