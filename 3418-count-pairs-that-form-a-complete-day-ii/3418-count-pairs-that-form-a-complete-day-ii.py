class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hsh=defaultdict(int)
        count=0
        
        for i in hours:
            res=i%24
            if abs(res-24)%24 in hsh:
                count+=hsh[abs(res-24)%24]
                
            hsh[res]+=1
        return count