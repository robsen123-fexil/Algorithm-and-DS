class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i , val in enumerate(arr):
            if val*2 in arr[i+1:] or val*2 in arr[:i]:
                return True
        return False
