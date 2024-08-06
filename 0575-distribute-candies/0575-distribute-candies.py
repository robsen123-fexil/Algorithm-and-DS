class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        half=len(candyType)//2
        
        hsh=set(candyType)
        minima=min(len(hsh) , half)
        return minima
        
        