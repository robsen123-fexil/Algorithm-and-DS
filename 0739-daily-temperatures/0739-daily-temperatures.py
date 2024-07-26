class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp=temperatures
        result=[0]*len(temp)
        stack=[]
        for i , val in enumerate(temp):
            while stack and stack[-1][1]<val:

                result[stack[-1][0]]=i-stack[-1][0]
                stack.pop()
            stack.append([i , val])
        return result
        