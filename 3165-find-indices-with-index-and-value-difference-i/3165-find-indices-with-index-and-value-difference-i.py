class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i , len(nums)):
                if abs(i-j)>=indexDifference and abs(nums[i]-nums[j])>=valueDifference:
                    return [i ,j]
        return [-1 , -1]


        
















        # l=0
        # r=len(nums)-1
        # hsh={}
        # for i , val in  enumerate(nums):
        #     hsh[val]=i
        # nums.sort()
        # while l<=r:
        #     if abs(l-r) >=indexDifference and abs(nums[l]-nums[r])>=valueDifference:
        #         return [hsh[nums[l]] , hsh[nums[r]]]
        #     elif abs(nums[l]-nums[r])<valueDifference:
        #         l+=1
        #     elif abs(l-r)<=indexDifference:
        #         r-=1

        # return [-1 , -1]
            

