class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        mn=int(len(arr)*0.05)
       
        
        arr=arr[mn:]  
        arr=arr[:-mn] 
        print(arr)
        sm=sum(arr)
        l=len(arr)
        return sm/l
        