class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        result=set()
        for a in range(int(math.sqrt(c))+1):
            b=int(math.sqrt(c-pow(a,2)))
            if pow(b , 2) + pow(a , 2)==c:
                result.add(b)
                result.add(a)
        return True if result else False

        