class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        l=r=0
        w1=list(word1)
        w2=list(word2)
        result=""
        while l<len(w1) and r<len(w2):
            if w1[l:]>w2[r:]:
                result+=(w1[l])
                l+=1
            else:
                result+=w2[r]
                r+=1
        while l<len(w1):
            result+=w1[l]
            l+=1
        while r<len(w2):
            result+=w2[r]
            r+=1
        return result


