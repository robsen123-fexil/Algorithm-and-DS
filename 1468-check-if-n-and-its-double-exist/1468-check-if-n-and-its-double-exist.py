class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            for j in range(len(arr)):

                if i!=j and arr[i]==arr[j]*2:
                    return True
        return False
                    