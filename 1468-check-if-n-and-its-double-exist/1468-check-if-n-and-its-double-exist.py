class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hsh={}
        for i in arr:
            if i*2 in hsh or i/2 in hsh:
                print(i  , hsh) 
                return True

            hsh[i]=1
        return False