class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hsh={}
        nums.sort()
        val=len(nums)//2
        count=0
        for i in nums:
            if i in hsh:
                hsh[i]+=1
            else:
                hsh[i]=1
        print(hsh , val)
        for key  , values in hsh.items():
            value = hsh.get(key)
            print(value , key)
            if value>val:
                return key

        

        