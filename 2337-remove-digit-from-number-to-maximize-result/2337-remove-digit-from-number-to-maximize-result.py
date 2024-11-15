class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res=[]
        nums=list(number)
        for i , val in enumerate(nums):
            if val==digit:
                res.append(i)
        maxima=float('-inf')
        print(res)
        for i in range(len(res)):
            val=""
            for j in range(len(nums)):
                if j!=res[i]:
                    val+=nums[j]
            print(val)
            maxima=max(maxima , int(''.join(val)))
        return str(maxima)