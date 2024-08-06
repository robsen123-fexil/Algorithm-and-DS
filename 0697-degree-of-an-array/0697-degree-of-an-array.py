class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hsh=Counter(nums)
        res=dict(sorted(hsh.items() , key=lambda x:x[1] , reverse=True ))
        high=0
        for i , val in res.items():
            high=val
            break
        result={}
        for i , val in res.items():
            if high==val:
                result[i]=val
        sol=defaultdict(list)
        for i , val in enumerate(nums):
            if val in result:
                sol[val].append(i)
        
        print(sol)
        minima=float('inf')
        for key , value in sol.items():
            mini=min(value)
            maxi=max(value)+1
            minima=min(minima , (maxi-mini))
        print(minima)
        return minima
        

            

        