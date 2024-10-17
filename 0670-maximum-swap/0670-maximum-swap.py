class Solution:
    def maximumSwap(self, num: int) -> int:
        maxima=num
        
        num=str(num)
        if len(num)==1:
            return int(''.join(num))
        num=list(num)
        
        for i in range(len(num)):
            for j in range(i+1 , len(num)):
                num[i] , num[j]=num[j],num[i]
                maxima=max(maxima , int(''.join(num)))
                num[i] , num[j] = num[j], num[i]
        return maxima