class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        answer=[0]*len(temperatures)
        for  i , t  in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackval, stackind =stack.pop()
                answer[stackind]=(i-stackind)
            stack.append([t, i])
        return answer
       