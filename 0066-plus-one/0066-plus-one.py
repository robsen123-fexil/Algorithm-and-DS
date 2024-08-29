class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # num = int(''.join(map(str, digits)))
        # num += 1
        # nums = list(map(int, str(num)))
        # return nums
        strs=""
        for i in digits:
            strs+=(str(i))
        integ=str(int(strs)+1)
        res=' '.join(integ)
        result=res.split()
        sol=[]
        for i in result:
            sol.append(int(i))
        return sol
                    