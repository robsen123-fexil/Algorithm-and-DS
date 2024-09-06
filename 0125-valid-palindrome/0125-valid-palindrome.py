class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs=""
        for i in s:
            if i.isalpha():

                strs+=i.lower()
            elif i.isdigit():
                strs+=i

        l=0
        
        print(strs)
        cnt=0
        
       
        r=len(strs)-1
        print(strs)
        while l<r:
            cnt+=strs[l]!=strs[r]
            l+=1
            r-=1
        return cnt==0