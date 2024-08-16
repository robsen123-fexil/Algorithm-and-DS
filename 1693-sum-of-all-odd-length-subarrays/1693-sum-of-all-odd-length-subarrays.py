class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sums=0
        for i in range(len(arr)):  
            for j in range(i , len(arr)):
                if (j-i+1)%2!=0:
                    sums+=sum(arr[i:j+1])
        return sums
