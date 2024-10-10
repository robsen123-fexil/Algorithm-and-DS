class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        nums=[]
        for i in arr:
            if i%2==0:
                nums.append(0)
            else:
                nums.append(1)
        hsh={0:1 , 1:0}
        count=sums=0
        mod=10**9 + 7
        for i in nums:
            sums+=i
            val=sums%2
            count+=hsh[1-val]
            hsh[val]+=1
        return count%mod
