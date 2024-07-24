class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l , r=0 , len(skill)-1
        result=0
        target=skill[r]+skill[l]
        while l<r:
            val=skill[r]+skill[l]
            if val!=target:
                return -1
            result+=(skill[l]*skill[r])
            l+=1
            r-=1
        return result



        