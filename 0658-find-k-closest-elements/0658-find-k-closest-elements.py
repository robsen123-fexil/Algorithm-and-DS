class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        hsh=defaultdict(list)
        for i in range(len(arr)):
            val=abs(x-arr[i])
            hsh[val].append(arr[i])
        result=[]
        dicti=dict(sorted(hsh.items() ,key=lambda x:x[0] ))
        print(dicti)
        for key , val in dicti.items():
            for i in range(len(val)):
                result.append(val[i])
        
        return sorted(result[:k])
            
        
            