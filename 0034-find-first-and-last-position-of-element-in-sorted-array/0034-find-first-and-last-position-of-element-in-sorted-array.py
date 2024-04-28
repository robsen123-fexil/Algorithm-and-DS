class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r=0, len(nums)-1
        ans=[]
        we_get = -1
        while l<=r:
            mid=(l+r) // 2
            if nums[mid] < target:
                l=mid+1
            elif nums[mid] > target:
                r=mid-1
            else:
                we_get = mid
                r = mid-1
        ans.append(we_get)
        we_get = -1
        l,r=0, len(nums)-1
        while l<=r:
            mid=(l+r) // 2
            if nums[mid] < target:
                l=mid+1
            elif nums[mid] > target:
                r=mid-1
            else:
                we_get = mid
                l = mid+1
        ans.append(we_get)

        return ans
        # l=0
        # ans=[]
        # r=len(nums)-1
        # we_get=-1
        # while l <=r:
        #     mid=(l+r) // 2
        #     if nums[mid] < target:
        #         l=mid+1
        #     elif nums[mid] > target:
        #         r=mid-1
        #     else:
        #         we_get=mid
        #         r=mid-1
        # ans.append(we_get)
       
        # we_get=-1
        # l=0
        # r=len(nums)-1
        # while l<r:
        #     mid=(l+r) // 2
        #     if nums[mid] < target:
        #         l=mid+1
        #     elif nums[mid]> target:
        #         r=mid-1
        #     else:
        #         we_get=mid
        #         l=mid+1
        # ans.append(we_get)
        # return sorted(ans)
             
       


       
        

    