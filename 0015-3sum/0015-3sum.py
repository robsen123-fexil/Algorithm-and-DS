class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # length=len(nums)
        # res=[] 
        # nums.sort()
        # for i in range(length-2):
        #     if i>0 and nums[i]==nums[i-1]:
        #        continue
        #     l=i+1
        #     r=length-1
        #     while l<r:
        #         total=nums[i]+nums[l]+nums[r]
        #         if total<0:
        #             l=l+1
        #         elif total>0:
        #             r=r-1
        #         else:
        #             res.append([nums[i], nums[l], nums[r]]) 
        #             while l<r and nums[l]==nums[l+1]:
        #                 l=l+1
        #             while l<r and nums[r]==nums[r-1]:
        #                 r=r-1   

        #             l=l+1
        #             r=r-1     

        # return res  
        # result=[]
        # nums.sort()
        # for i , a in enumerate(nums):
        #     if i>0 and a==nums[i-1]:
        #         continue
        #     hsh={}            
        #     for j  , value in enumerate(nums[i+1:]):
        #         b=-a-value
        #         if b in hsh:
        #             if not [a , value , b] in result:
        #                 result.append([a , value , b])
        #         hsh[value]=j
        # return result
        result=[]
        nums.sort()
        for i , a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                total=a+nums[l]+nums[r]
                if total<0:
                    l+=1
                elif total>0:
                    r-=1
                else:
                    result.append([a , nums[l] , nums[r] ])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                    
                    r-=1
                    while nums[r]==nums[r+1] and l<r:
                        r-=1

        return result


