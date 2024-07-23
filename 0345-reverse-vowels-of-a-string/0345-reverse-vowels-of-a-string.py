class Solution:
    def reverseVowels(self, s: str) -> str:
        l=0
        ss=list(s)
        r=len(ss)-1
        vow=['a' , 'e' , 'i', 'o' , 'u' , 'A' , 'E' , 'O'  , 'I' , 'U']
        while r>l:
            if ss[l] in vow:
                while r>l:
                    if ss[r] in vow:
                        ss[l] , ss[r] = ss[r] , ss[l]
                        l+=1
                        r-=1
                        break
                    r-=1
            elif ss[r] in vow:
                while r>l:
                    if ss[l] in vow:
                        ss[l] , ss[r]=ss[r] , ss[l]
                        l+=1
                        r-=1
                        break
                    l+=1
            else:
                l+=1
                r-=1
        return ''.join(ss)