class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        res=[]
        for i in messages:
            res.append(len(i.split()))
        print(res)
        hsh={}
        l=0
        for i in senders:
            if i not in hsh:
                hsh[i]=res[l]
                l+=1
            else:
                hsh[i]+=res[l]
                l+=1
        counts=[]
        maxima=max(hsh , key=hsh.get)
        vall=hsh[maxima]
        for val in hsh.values():
            counts.append(val)
        cntcount=Counter(counts)
        
        resuu=[]
        if cntcount[vall]==1:
            return maxima
        for key , value in hsh.items():
            if value==vall:

                resuu.append(key)
        srt=sorted(resuu)
        print(resuu)

        
        
        return srt[-1]