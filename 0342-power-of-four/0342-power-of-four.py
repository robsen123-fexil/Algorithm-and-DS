class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def helperfunction(n):
            if n==1:
                return True
            if n<4:
                return False
            return helperfunction(n/4)
        return helperfunction(n)