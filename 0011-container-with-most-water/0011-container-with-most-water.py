class Solution:
    def maxArea(self, height: List[int]) -> int:
        # l=0
        # r=len(height)-1
        # maxima=float("-inf")
        # while l<r:
        #     leng=(r-l)
        #     if height[l]>height[r]:
        #         h=height[r]
        #         r-=1
        #     else:
        #         h=height[l]
        #         l+=1
        #     maxima=max(maxima, leng*h)
        # return maxima
        
        # l=0
        # maxima=float('-inf')
        # for i in range(len(height)):
        #    r = len(height)-1
        #    while i < r:
        #       leng = r - i
        #       value = min(height[i], height[r])
        #       maxima = max(maxima, value * leng)
        #       r -= 1
        # return maxima
        l , r , maxima = 0 , len(height)-1 , 0
        while l<r:
            leng=r-l
            value=min(height[l] , height[r])
            maxima=max(maxima , value*leng)
            if height[r]<height[l]:
                r-=1
            elif height[r]==height[l]:
                r-=1
            else:
                l+=1
        return maxima
            
