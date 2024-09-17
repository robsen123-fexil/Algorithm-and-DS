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
        result=[]
        for key , val in hsh.items():
            if vall==val:
                result.append(key)
        srt=sorted(result)
        return srt[-1]