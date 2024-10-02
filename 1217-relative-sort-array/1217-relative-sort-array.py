class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt=Counter(arr1)
        result=[]
        right=[]
        l=r=0
        for i in range(len(arr2)):
            
            result.extend([arr2[i]]*cnt[arr2[i]])
        for i in arr1:
            if i not in result:
                right.append(i)
        return result+sorted(right)
