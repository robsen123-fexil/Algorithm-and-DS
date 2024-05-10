class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        resu=sorted(hashmap.items() , key =lambda x:(-x[1], x[0]))
        print(resu)
        result=[]
        for k , v in resu:
            if v ==2:
                result.append(k)
        return result
