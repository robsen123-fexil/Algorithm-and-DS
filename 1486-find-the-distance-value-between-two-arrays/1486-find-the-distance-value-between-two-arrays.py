class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count=0
        for i in arr1:
            l=0
            for j in arr2:
                res=abs(i-j)
                if res<=d:
                    break
                l+=1
            if l==len(arr2):
                count+=1
        return count