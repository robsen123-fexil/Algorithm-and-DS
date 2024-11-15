class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hsh={}
        for i , val in enumerate(s):
            hsh[val]=i
        print(hsh)
        maxima=0
        strs=""
        res=[]
        for i in range(len(s)):
            maxima=max(maxima , hsh[s[i]])
            strs+=s[i]
            if maxima==i:
                res.append(len(strs))
                strs=""
        return res


        