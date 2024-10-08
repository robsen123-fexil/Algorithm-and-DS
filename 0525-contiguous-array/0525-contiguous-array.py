class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hsh={0:-1}
        num=[]
        for i in nums:
            if i==0:
                num.append(-1)
            else:
                num.append(1)
        ans=sums=0
        print(num)
        for i in range(len(num)):
            sums+=num[i]
            if sums in hsh:
                ans=max(ans , i-hsh[sums])
            elif sums not in hsh:
                hsh[sums]=i
        return ans