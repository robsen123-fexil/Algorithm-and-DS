class Solution:
    def romanToInt(self, s: str) -> int:
        hsh={'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100  , 'D':500 , 'M':1000}
        result=[]
        for i in s:
            value=hsh.get(i)
            result.append(value)
        print(result)
        stack=[]
        for i in result:
            if stack and stack[-1]<i:
                value=i-stack.pop()
                stack.append(value)
            else:
                stack.append(i)
        return sum(stack)
    
        