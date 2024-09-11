class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        perm=[]
        def helper(num):
            if num==1:
                return True
            if num==0 or num%2!=0:
                return False
            return helper(num//2)
        for i in itertools.permutations(str(n)):
            if i[0]!='0':
                num=int(''.join(i))
                if helper(num):
                    return True
        return False