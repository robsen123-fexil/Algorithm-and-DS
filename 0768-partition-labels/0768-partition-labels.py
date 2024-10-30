class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hsh={}
        for i  , val in enumerate(s):
            hsh[val]=i
        maxima=hsh[s[0]]
        strs=""
        res=[]
        for i in range(len(s)):
            maxima=max(maxima , hsh[s[i]])
            strs+=s[i]
            if i==maxima:
                print(strs)
                res.append(len(strs))
                strs=""
            
        return res
            