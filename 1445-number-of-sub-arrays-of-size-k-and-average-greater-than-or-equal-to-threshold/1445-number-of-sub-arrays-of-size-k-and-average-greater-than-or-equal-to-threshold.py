class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res=sum(arr[:k])
        avg=res//k
        count=0
        if avg>=threshold:
            count+=1
        l=0
        for i in range(k , len(arr)):
            res-=arr[l]
            l+=1
            res+=arr[i]
            if res//k>=threshold:
                count+=1
            
        return count