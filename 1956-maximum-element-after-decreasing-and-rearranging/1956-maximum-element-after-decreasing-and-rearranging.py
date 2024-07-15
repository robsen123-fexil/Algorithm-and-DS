class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0]=1
        result=[arr[0]]
        for i in range(1 , len(arr)):
            arr[i]= min(arr[i] , arr[i-1]+1)
            result.append(arr[i])
        return max(result)
        