class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l=len(nums)
        a=l//3
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        res=[]
        for key , value in hashmap.items():
            if value > a:
                res.append(key)
        return res
                
        