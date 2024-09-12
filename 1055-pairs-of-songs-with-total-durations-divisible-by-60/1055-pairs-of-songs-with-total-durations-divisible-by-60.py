class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time.sort()
        hsh=defaultdict(int)
        cnt=0
        for i in time:
            res=i%60
            if abs(res-60)%60 in hsh:
                cnt+=hsh[abs(res-60)%60]
            hsh[res]+=1
        return cnt