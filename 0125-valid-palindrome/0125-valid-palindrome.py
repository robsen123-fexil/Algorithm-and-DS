class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=""
        fina=""
        for i in s:
            if i.isalnum():
                result+=i
        res=result.lower()
        for i in range(len(res)-1, -1, -1):
            fina+=res[i]
        if fina==res:
            return True
        else:
            return False