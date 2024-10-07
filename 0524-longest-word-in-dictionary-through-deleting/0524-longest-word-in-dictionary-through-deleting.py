class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        result=[]
        for i in range(len(dictionary)):
            l=0
            r=0
            while l<len(dictionary[i]) and r<len(s):
                if dictionary[i][l]==s[r]:
                    l+=1
                r+=1
            if l==len(dictionary[i]):
                result.append(dictionary[i])
        srt=sorted(result , key=lambda x:(-len(x) , x))
        return srt[0] if srt else ""
            