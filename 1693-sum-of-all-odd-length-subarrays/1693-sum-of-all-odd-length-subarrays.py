class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sums=0
        for i in range(len(arr)):

            
            for j in range(i+1 , len(arr)+1):
                sub=arr[i:j]
                if len(sub)%2!=0:
                    res=sub[:]
                    print(sub)
                    sums+=sum(res)
        return sums
                    