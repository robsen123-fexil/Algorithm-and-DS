class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref=[1]
        num=nums[::-1]
        for i in range(len(num)):
            pref.append(pref[-1]*num[i])
        suffix=[1]
        for i in range(len(nums)-1):
            suffix.append(suffix[-1]*nums[i])
        pref.pop()
        numb=pref[::-1]
        result=[]
        for i in range(len(numb)):
            result.append(numb[i]*suffix[i])
        print(result)
        print(suffix ,numb)

        return result
       
