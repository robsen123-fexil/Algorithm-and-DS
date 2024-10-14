class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        val=inf
        result=[]
        arr.sort()
        for i in range(1 , len(arr)):
            val=min(val , arr[i]-arr[i-1])
        res=arr[:2]
        a , b =res
        minima=b-a
        if minima==val:
            result.append([a, b])
        l=0
        for i in range(2 , len(arr)):
            res.append(arr[i])
            res.remove(arr[l])
            l+=1
            a , b =res
            minima=b-a
            if minima==val:
                result.append([a , b])
        return result
            