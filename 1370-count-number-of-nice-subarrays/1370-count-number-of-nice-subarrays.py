class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        num=[]
        for i in nums:
            if i%2==0:
                num.append(0)
            else:
                num.append(1)
        res=l=maxima=count=sums=0
        hsh={0:1}
        for i in range(len(num)):
            sums+=num[i]
            if sums-k in hsh:
                count+=hsh[sums-k]
            if sums not in hsh:
                hsh[sums]=1
            else:
                hsh[sums]+=1
        return count