class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        maxima=max(arr)
        ind=arr.index(maxima)
        
        if ind ==0 or ind==len(arr)-1:
            print(ind)
            return False
        
        l=1
        r=len(arr)-1
        while l<ind:
            if arr[l]<=arr[l-1]:
                print('l')
                return False
            l+=1
        while r>ind:
            if arr[r]>=arr[r-1]:
                print("r")
                return  False
            r-=1
        return True
                