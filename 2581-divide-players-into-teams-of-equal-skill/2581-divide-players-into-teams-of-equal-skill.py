class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l=0
        r=len(skill)-1
        skill.sort()
        res=skill[l]+skill[r]
        result=0
        while l<r:
            if skill[l]+skill[r]==res:
                result+=(skill[l]*skill[r])
            else:
                return -1
            r-=1
            l+=1
        return result

