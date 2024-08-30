class Solution:
    def nextGreaterElement(self, n: int) -> int:
        strs=str(n)
        perm=list(itertools.permutations(strs))
        result=[]
        for i in perm:
            if len(''.join(i))==len(str(n)):
               result.append(int(''.join(i)))
        result.sort()
        MIN_INT_32 = -2**31
        MAX_INT_32 = 2**31 - 1
        for i in result:
            if n<i:
                if MIN_INT_32 <= i <= MAX_INT_32:
                    return i
                else:
                    
                    return -1
                
        return -1