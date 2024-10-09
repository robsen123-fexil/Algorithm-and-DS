class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        res=[]
        count=0
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            elif stack and stack[-1]=='(' and s[i]==')':
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack)
