class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hsh=defaultdict(int)
        count=0
        for i in hours:
            res=i%24
            diff=abs(res-24)%24
            if diff in hsh:
                count+=hsh[diff]
            hsh[res]+=1
        return count