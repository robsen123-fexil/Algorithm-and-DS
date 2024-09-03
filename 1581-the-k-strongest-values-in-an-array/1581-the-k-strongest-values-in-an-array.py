class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        md=(len(arr)-1)//2
        mid=arr[md]
        l=0
        r=len(arr)-1
        result=[]
        while l<=r:
            res=abs(arr[l]-mid)
            res2=abs(arr[r]-mid)
            if res>res2:
                result.append(arr[l])
                l+=1
            else:
                result.append(arr[r])
                r-=1
        return result[:k]
        
