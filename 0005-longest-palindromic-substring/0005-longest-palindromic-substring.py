class Solution:
    def longestPalindrome(self, s: str) -> str:
        result=[]
        def ispalindrom(res):
            return res==res[::-1]
        for i in range(len(s)):
            for j in range(i+1 , len(s)+1):
                res=s[i:j]
                if ispalindrom(res) :
                    result.append(res)
        resu=sorted(result , key=lambda x:len(x)  , reverse=True)
        if len(resu)==0:
            return ""
        else:
            return resu[0]
        return resu[0]
        


        
        

        