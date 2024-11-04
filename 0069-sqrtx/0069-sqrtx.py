class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x+1):
            
            if i**2 == x:
                return i
            elif i**2 > x:
                return i-1
        
        return 0