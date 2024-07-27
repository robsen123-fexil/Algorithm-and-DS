class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        s=list(s)
        # for i in s:
        #     if i =='(' or i == '{' or i == '[':
        #         stack.append(i)
        #     else:
        #         if i==')':
        #             if stack and stack[-1]=='(':
        #                 stack.pop()
        #             else:
        #                 return False 
        #         if i=='}':
        #             if stack and stack[-1]=='{':
        #                 stack.pop()
        #             else:
        #                 return False
        #         if i==']':
        #             if stack and stack[-1]=='[':
        #                 stack.pop()
        #             else:
        #                 return False 
        # if not stack:
        #     return True       
        # for i in s:
        #     if stack :
        #         if stack[-1]=='(' or stack[-1]=='[' or stack[-1]=='}':
        #             if i==')':
        #                 stack.append(i)
        #             else:
        #                 return False
        #         if stack[-1]=='{':
        #             if i=='}':
        #                 stack.append(i)
        #             else:
        #                 return False
        #         if stack[-1]=='[':
        #             if i==']':
        #                 stack.append(i)
        #             else:
        #                 return False
                    
                
        #     else:
        #         stack.append(i)
        # return True
        if len(s)==1:
            return False
        for i in s:
            if i == '{' or i=='[' or i=='(':
                stack.append(i)
            else:
                if stack:
                    if i==')' and stack[-1]=='(':
                        stack.pop()
                    
                    elif  i=='}' and stack[-1]=='{':
                        stack.pop()
                    
                    elif i==']' and stack[-1]=='[':
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(i)
        return True if not stack else False
        