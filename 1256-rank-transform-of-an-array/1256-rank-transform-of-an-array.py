class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hsh={}
        l=1
        nums=sorted(arr)
        for i in range(len(nums)):
            if nums[i] not in hsh:
                hsh[nums[i]]=l
                l+=1
        result=[]
        for i in range(len(arr)):
            result.append(hsh[arr[i]])
        return result