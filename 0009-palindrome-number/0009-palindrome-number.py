class Solution:
    def isPalindrome(self, x: int) -> bool:
       if x<0:
         return 0
       y=list(map(int, str(x)))
       z=y[::-1]
       if y == z:
          return True
       else:
          return False
       