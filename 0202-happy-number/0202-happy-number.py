class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        def helper(n , seen):
            
            if n==1:
                return True
            if n in seen:
                return False
            seen.add(n)
            strs=str(n)
            value=0
            for i in strs:
                value+=(int(i)**2)
            return helper(value , seen)
        return helper(n , seen)
        
        