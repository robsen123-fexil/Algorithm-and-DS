class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        l=0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i!=j and arr[i]==(2*arr[j]):
                    return True
            
        return False