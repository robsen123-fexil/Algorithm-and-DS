class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            l=0
            while l<len(arr):
                if l!=i and arr[i]==arr[l]*2:
                    return True
                l+=1
        return False
