class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        hashmap1 ={}
        for i in nums:
            if i in hashmap1:
                hashmap1[i]+=1
            else:
                hashmap1[i]=1
        return min(hashmap1, key=hashmap1.get)
        
      


        
