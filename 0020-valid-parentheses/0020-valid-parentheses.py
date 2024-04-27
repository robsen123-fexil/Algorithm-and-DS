class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        s=list(s)
        for i in s:
            if i =='(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if i==')':
                    if stack and stack[-1]=='(':
                        stack.pop()
                    else:
                        return False 
                if i=='}':
                    if stack and stack[-1]=='{':
                        stack.pop()
                    else:
                        return False
                if i==']':
                    if stack and stack[-1]=='[':
                        stack.pop()
                    else:
                        return False 
        if not stack:
            return True       
 
                

                

            

        


