class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        hsh=[]
        
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
                hsh.append(i)
            elif stack and stack[-1]=='(' and s[i]==')':
                
                stack.pop()
                hsh.pop()
            elif s[i]==')':
                hsh.append(i)
            else:
                continue
        
        s=list(s)
        res=[]
        for i in sorted(hsh , reverse=True):
            s.pop(i)
        return ''.join(s)
        