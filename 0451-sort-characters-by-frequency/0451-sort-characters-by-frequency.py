class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap={}
        result=""
        for i in s:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        res={k:v for k , v in sorted(hashmap.items() , key = lambda item:item[1], reverse=True)}
        for key , value in res.items():
            for i in range(value):
                result+=key
        return result