class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        leng=len(s1)
        s1=sorted(s1)
        res=list(s2[:leng])
        if sorted(''.join(res))==s1:
            return True
        l=0
        for i in range(leng , len(s2)):
            res.append(s2[i])
            res.remove(s2[l])
            l+=1
            if sorted(''.join(res))==s1:
                return True
            
        return False




        return 0