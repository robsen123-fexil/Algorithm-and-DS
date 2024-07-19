class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result={}
        nums.sort()
        
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                
                if total>target:
                    diff=total-target
                    result[diff]=total
                    r-=1
                elif total<target:
                    diff=target-total
                    result[diff]=total
                    l+=1
                else:
                    return target
        print(result)
        return result[min(result)]    