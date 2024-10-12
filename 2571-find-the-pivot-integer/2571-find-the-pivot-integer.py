class Solution:
    def pivotInteger(self, n: int) -> int:
        sums=0
        for i in range(1 , n+1):
            sums+=i
        sms=0
        for i in range(1 , n+1):
            sms+=i
            if sums==sms:
                return i
            else:
                sums-=i
        return -1