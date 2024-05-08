class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        n=len(nums)
        a=n//2
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        for key , value in hashmap.items():
            if value > a:
                return key 
    