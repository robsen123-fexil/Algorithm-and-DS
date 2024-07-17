class Solution:
    def longestPalindrome(self, s: str) -> str:
        result=[]
        def ispalindrom(res):
            return res==res[::-1]
        for i in range(len(s)):
            # for j in range(i+1 , len(s)+1):
            j=i+1
            while j<len(s)+1:
                res=s[i:j]
                if ispalindrom(res) :
                    result.append(res)
                j+=1
        resu=sorted(result , key=lambda x:len(x)  , reverse=True)
        if len(resu)==0:
            return ""
        else:
            return resu[0]
        return resu[0]

        # result=[]
        # def ispalindrome(res):
        #     return res==res[::-1]
        
        # for i in range(len(s)):
        #     r=i+1
        #     strs=''
        #     while r<len(s)+1:
        #         res=s[i:r]
        #         if ispalindrome(res):
        #             result.append(res)
        #         r+=1
        # result=sorted(result , key= lambda x:len(x) , reverse=True)
        # print(result)
        # return result[0] if len(result)!=0 else ""
        


        
        

        