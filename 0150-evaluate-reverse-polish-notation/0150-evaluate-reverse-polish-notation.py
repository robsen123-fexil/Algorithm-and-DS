class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        oper=["+" , '/' , '*' , '-']
        for i in range(len(tokens)):
            if tokens[i] not in oper:
                stack.append(int(tokens[i]))
            else:
                a=stack.pop()
                b=stack.pop()
                if tokens[i]=='+':
                    stack.append(b+a)
                elif tokens[i]=='/':
                    stack.append(int(b/a))
                    
                elif tokens[i]== '-':
                    stack.append(b-a)
                else:
                   
                    stack.append(b*a)
                    
        
        return stack[0]