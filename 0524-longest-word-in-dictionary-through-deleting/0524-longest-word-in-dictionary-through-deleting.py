class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res=[]
        for i in range(len(dictionary)):
            l=0
            r=0
            while l<len(s) and r<len(dictionary[i]):
                if s[l]==dictionary[i][r]:
                    r+=1
                l+=1
            if r==len(dictionary[i]):
                res.append(dictionary[i])
        srt=sorted(res , key=lambda x:(-len(x) , x))
        return srt[0] if srt else ""
        
    