class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a' , 'e' , 'i' , 'o' , 'u']
        l=0
        r=len(s)-1
        s=list(s)
        while l<r:
            while l<r and s[l].lower() not in vowels:
                l+=1
            while r>l and s[r].lower() not in vowels:
                r-=1
            s[r] , s[l]=s[l] , s[r]
            r-=1
            l+=1
        return ''.join(s)