class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)):
            for k in range(i+1 , len(nums)):
                l=k+1 
                r=len(nums)-1
                while l<r:
                    total=nums[i]+nums[k]+nums[l]+nums[r]
                    if total<target:
                        l+=1
                    elif total>target:
                        r-=1
                    else:
                        if [nums[i] , nums[k] , nums[l] , nums[r] ] not in result:

                            result.append([nums[i] , nums[k] , nums[l] , nums[r] ])
                        l+=1
        return result        