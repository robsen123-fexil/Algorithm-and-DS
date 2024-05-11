class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap={}
        for i in range(len(names)):
            hashmap[heights[i]]=names[i]
        res=sorted(hashmap.items()  , key =lambda x:(-x[0]))
        result=[]
        for k , v in res:
            result.append(v)
        return result


