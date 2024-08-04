class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hsh=defaultdict(list)
        # for i in range(len(nums)):
        #     if i in hsh:
        #         hsh[nums[i]].append(i)
        #     else:
        #         hsh[nums[i]].append(i)
        # for key , value in hsh.items():
        #     for j in range(1 , len(value)):
        #         if abs(value[j]-value[j-1])<=k:
        #             return True
        # return False  
        # print(hsh)
        # return 0
        hsh={}
        for i in range(len(nums)):
            if nums[i] in hsh:
                if abs(i-hsh[nums[i]])<=k:
                    return True
            hsh[nums[i]]=i
        return False
            