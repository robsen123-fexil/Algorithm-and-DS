class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm=list(permutations(s1))
        result=[]
        for i in perm:
            result.append(''.join(i))
        s2=list(s2)
        res=s2[:len(s1)]
        if ''.join(res) in result:
            return True
        l=0
        
        for i in range(len(s1) , len(s2)):
            res.remove(s2[l])
            res.append(s2[i])
            
            if ''.join(res)  in result:
                return True
            l+=1
        else:
            return False