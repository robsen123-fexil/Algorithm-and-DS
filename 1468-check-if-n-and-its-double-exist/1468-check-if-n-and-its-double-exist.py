class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr)):
            l=0
            r=len(arr)-1
            while l<=r:
                mid=(l+(r-l)//2)
                res=2*(arr[mid])
                if mid!=i and res==arr[i]:
                    return True
                elif res>arr[i]:
                    r=mid-1
                elif res<arr[i]:
                    l=mid+1
                else:
                    break
        return False
                

