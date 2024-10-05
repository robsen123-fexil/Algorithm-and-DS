class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxima=float('-inf')
        while l<r:
            minima=min(height[l] , height[r])
            area=minima*(r-l)
            maxima=max(maxima , area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxima