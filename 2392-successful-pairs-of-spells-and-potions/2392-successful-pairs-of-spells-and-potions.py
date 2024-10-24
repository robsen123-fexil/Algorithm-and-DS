class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result=[]
        potions.sort()
        for i in spells:
            l=0
            r=len(potions)-1
            while l<=r:
                mid=(r+l)//2
                if i*potions[mid]>=success:
                    r=mid-1
                else:
                    l=mid+1
            result.append(len(potions)-l)
            
        return result