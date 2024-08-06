class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hsh={}
        for i , val in enumerate(list1):
            hsh[val]=i
        result={}
        for i , val in enumerate(list2):
            if val in hsh:
                value=hsh.get(val)
                result[val]=i+value
        res=dict(sorted(result.items() , key=lambda x:x[1]))
       
        solution=[]
        first=0
        print(res)
        for key , value in res.items():
            first=res.get(key)
            print(first)
            break
        
        for key , value in res.items():
            
            if first==value:
                
                solution.append(key)
        return solution