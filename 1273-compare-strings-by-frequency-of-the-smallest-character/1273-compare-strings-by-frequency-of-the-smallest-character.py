class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        strs1=[]
        hsh={}
        for i in queries:
            cnt=Counter(i)
            minima=min(i)
            val=cnt[minima]
            strs1.append([minima , val])
        
        strs2=[]
        result=[]
        for i in words:
            cnt=Counter(i)
            minima=min(i)
            val=cnt[minima]
            strs2.append([minima , val])
        for i in range(len(strs1)):
            count=0
            a , b=strs1[i]
            for j in range(len(strs2)):
                x , y= strs2[j]
                if y>b:
                    count+=1
            result.append(count)
        return result
