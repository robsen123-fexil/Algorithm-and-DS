class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l=0
        s=list(s)
        r=len(s)-1
        alp=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' , 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

        while l<r:
            while s[l] not in alp and l<r:
                l+=1
            while s[r] not in alp and r>l:
                r-=1
            s[l] , s[r]=s[r] , s[l]
            l+=1
            r-=1
        return ''.join(s)

    