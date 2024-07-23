class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # count=0
        # result=[]
        # for i in range(len(nums)):
        #     for j in range(i+1  , len(nums)):
        #         val=abs(nums[i] -nums[j])
        #         if val==k:
        #             res=[nums[i] , nums[j]]
        #             res.sort()
        #             if  res not in result:
        #                result.append(res)
        # print(result)
        # return len(result)
        # l=0
        # r=len(nums)-1
        # count=0
        # nums.sort()
        # while l<len(nums)-1:
        #     while l<r:
        #         val=abs(nums[l]-nums[r])
        #         if val==k:
        #             count+=1
        #             break
        #         r-=1   
        #     while l<(len(nums)-1):
        #         if nums[l+1] !=nums[l]:
        #             l+=1
        #             break
        #         l+=1
        #     r=len(nums)-1
        # return count
        hsh=Counter(nums)
        print(hsh)
        count=0
        if k==0:
            for key, value in hsh.items():
                if value >1:
                    count+=1
        else:
            for key , value in hsh.items():
                if key+k in nums:
                    count+=1
        return count


        