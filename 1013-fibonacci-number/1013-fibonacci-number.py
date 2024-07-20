class Solution:
    def fib(self, n: int) -> int:
        result=[0 , 1]
        for i in range(n):
            result.append(result[-2]+result[-1])
        return result[-2]
        