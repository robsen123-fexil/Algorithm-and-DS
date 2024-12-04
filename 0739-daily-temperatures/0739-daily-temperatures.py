class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        temp=temperatures
        stack=[]
        for i in range(len(temp)):
            if stack:
                while stack and stack[-1][0]<temp[i]:
                    a , b = stack.pop()
                    result[b]=(i-b)
                stack.append([temp[i] , i])
            else:
                stack.append([temp[i] ,i])
        return result
