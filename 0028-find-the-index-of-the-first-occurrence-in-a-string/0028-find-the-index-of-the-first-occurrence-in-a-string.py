class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.index(haystack[needle[0]]) if needle in haystack else -1
        # if ''.join(needle) in haystack:
        #     res=haystack.index(haystack[needle[0]])
        # else:
        #     return -1
        # return res
        index=haystack.find(needle)
        return index
        