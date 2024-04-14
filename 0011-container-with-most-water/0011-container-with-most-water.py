class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxima=float("-inf")
        while l<r:
            leng=(r-l)
            if height[l]>height[r]:
                h=height[r]
                r-=1
            else:
                h=height[l]
                l+=1
            maxima=max(maxima, leng*h)
        return maxima
            
        
        