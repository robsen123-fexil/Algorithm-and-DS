class Solution:
    def minimumLength(self, s: str) -> int:
        l=0
        r=len(s)-1
        s=list(s)
        char=s[-1]
        while l<r:
            
            if s[l]!=s[r]:
                print(s[l] , s[r])
                break
            else:
                charl=s[l]
                while r>=l and s[l]==charl:
                    l+=1
                charr=s[r]
                while r>=l and s[r]==charr:
                    r-=1
            char=s[r]  
        return r-l+1
                
        return len(s)

