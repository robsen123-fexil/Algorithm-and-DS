class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxima=float('-inf')
        num=[]
        for i in nums:
            if i==0:
                num.append(-1)
            else:
                num.append(1)
        print(num)
        hsh={0:-1}
        sums=0
        target=0
        for i , val in enumerate(num):
            sums+=val
            diff=sums-target
            if diff in hsh:
                res=i-hsh[diff]
                maxima=max(maxima ,res )
            if diff not in hsh:
                hsh[diff]=i
        return maxima if maxima!=float('-inf') else 0




