class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        
        if not s:
            return 0
        neg=False
        out=0
        if s[0]=="-":
            neg=True
        elif s[0]=="+":
            neg=False
        elif not s[0].isnumeric():
            return 0
        else:
            out=ord(s[0])-ord("0") 
        for i in range(1, len(s)):
            if s[i].isnumeric():
                out=out*10 +( ord(s[i])-ord("0"))
                
                if not neg and out>=2147483647:
                   return 2147483647
                if neg and out>=2147483648:
                   return -2147483648
            else:
                break
        if not neg:
            return out
        else:
            return -out
        