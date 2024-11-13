class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        leng=len(needle)
        haystack=list(haystack)
        res=haystack[:leng]
        if ''.join(res)==needle:
            return 0
        l=0
        for i in range(leng , len(haystack)):
            res.append(haystack[i])
            res.remove(haystack[l])
            l+=1
            if ''.join(res)==needle:
                return abs(leng-i)+1
        return -1
