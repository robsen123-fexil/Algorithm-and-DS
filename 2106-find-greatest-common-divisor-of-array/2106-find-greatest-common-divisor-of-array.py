class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minima=min(nums)
        maxima=max(nums)
        res1=[]
        res2=[]
        for i in range(1 , int(minima**0.5)+1):
            if minima%i==0:
                res2.append(i)
                if i!=minima//i:
                    res2.append(minima//i)
        print(res2)
        for i in range(1 , int(maxima**0.5)+1):
            if maxima%i==0:
                res1.append(i)
                if i!=maxima//i:
                    res1.append(maxima//i)
        res=res1+res2
        print(res)
        cnt=Counter(res)
        print(cnt)
        result=[key for key , val in cnt.items() if val==2]
        result.sort()
        print(result)
        return result[-1]