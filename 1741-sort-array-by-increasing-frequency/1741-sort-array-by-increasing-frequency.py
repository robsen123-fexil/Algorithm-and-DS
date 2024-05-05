class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hashmap={}
        result=[]
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        res=sorted(hashmap.items(), key=lambda item: (item[1], -item[0]))
        print(hashmap)
        for key , value in res:
            for i in range(value):
                result.append(key)
        return result

        