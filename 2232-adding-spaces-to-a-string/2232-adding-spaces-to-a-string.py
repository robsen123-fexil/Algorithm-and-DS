class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        lists=['a']*(len(s)+len(spaces))
        for i in range(len(spaces)):
            lists[spaces[i]-1]=" "
        print(lists)
        l=r=0
        strs=""
        while l<len(s)  and r<len(spaces):
            if l!=spaces[r]:
                strs+=s[l]
            else:
                strs+=" "
                strs+=s[l]
                r+=1
            l+=1

        while l<len(s):
            strs+=s[l]
            l+=1
        return strs

