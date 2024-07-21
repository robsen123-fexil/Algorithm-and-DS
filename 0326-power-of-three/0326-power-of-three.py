class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def three(n):
            if n==1:
                return True
            if n<3:
                return False
            return three(n/3)
        return three(n)
        