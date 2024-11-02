class Solution:
    def addDigits(self, num: int) -> int:
        def helper(strs):
            if len(strs)==1:
                return int(strs)
            # val=strs.split()
            # res=0
            # for i in val:
            #     res+=(int(i))
            res=0
            for i in strs:
                res+=int(i)
            return helper(str(res))
        return helper(str(num))