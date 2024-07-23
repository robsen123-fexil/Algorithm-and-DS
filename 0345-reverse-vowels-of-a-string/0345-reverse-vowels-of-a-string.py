class Solution:
    def reverseVowels(self, s: str) -> str:
        l=0
        ss=list(s)
        r=len(ss)-1
        vow=['a' , 'e' , 'i', 'o' , 'u' , 'A' , 'U' ,'O' , 'I' , 'E']
        while r>l:
            while l<r and ss[l] not in vow:
                l+=1
            while l<r and ss[r] not in vow:
                r-=1
            ss[l] , ss[r] = ss[r] , ss[l]
            l+=1
            r-=1
        return ''.join(ss)
        