class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        strs=list(haystack)
        first=strs[:len(needle)]
        if ''.join(first)==needle:
            return 0
        l=0
        for i in range(len(needle) , len(strs)):
            first.remove(strs[l])
            first.append(strs[i])
            l+=1
            res=''.join(first)
            if res==needle:
                return l
        else:
            return -1