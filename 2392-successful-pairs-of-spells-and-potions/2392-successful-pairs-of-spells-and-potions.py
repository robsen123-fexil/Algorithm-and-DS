class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res=[]
        l=0
        potions.sort()
        def binary(i , potions):
            l=0
            r=len(potions)-1
            while l<=r:
                mid=(r+l)//2
                if potions[mid]*i>=success:
                    r=mid-1   
                else:
                    l=mid+1
            return l
        for i in spells:
            val=binary(i , potions)
            res.append(len(potions)-val)
        return res
                