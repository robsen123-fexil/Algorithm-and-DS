class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(n  , 2*n+1):
            print(i)
            if i%n==0 and i%2==0:
                return i
        return 0