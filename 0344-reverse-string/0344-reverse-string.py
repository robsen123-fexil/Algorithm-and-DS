class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # def helper(s , l , r):
        #     if l>r:
        #         return s
        #     s[l] , s[r]= s[r] , s[l]
            
        #     return helper(s , l+1 , r-1)
        # return helper(s , 0 , len(s)-1)
        l=0
        r=len(s)-1
        while l<r:
            s[l], s[r]=s[r] , s[l]
            l+=1
            r-=1
        