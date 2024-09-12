class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        hsh=defaultdict(list)
        for i , j in zip(values , labels):
            hsh[j].append(i)
        res=[]
        for key , values in hsh.items():
            val=sorted(values , reverse=True)
            res.append(val[:useLimit])
        result=[]
        for i in res:
            for j in i:
                result.append(j)
        resu=sorted(result , reverse=True)
        sums=sum(resu[:numWanted])

        l=0
        maxima=sums
        for i in range(numWanted , len(res)):
            sums+=resu[i]
            sums-=resu[l]
            l+=1
            maxima=max(maxima , sums)
        return maxima
