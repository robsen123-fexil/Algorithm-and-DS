class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        print(hashmap)
        res=sorted(hashmap.items() , key = lambda x:(-x[1] , x[0]))
        for k , v in res:
            if v==2:
                return k
            else :
                return k