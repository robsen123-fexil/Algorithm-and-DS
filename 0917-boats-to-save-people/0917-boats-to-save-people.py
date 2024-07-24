class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r=len(people)-1
        res=0
        while l<=r:
            val=people[l]+people[r]
            if val<=limit:
                res+=1
                r-=1
                l+=1
            else:
                res+=1
                r-=1
        return res

        