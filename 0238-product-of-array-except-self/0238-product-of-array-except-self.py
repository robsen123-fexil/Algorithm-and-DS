class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        bef=[]
        aft=[]
        bef.append(1)
        aft.append(1)
        for i in nums:
            bef.append(bef[-1]*i)
        for i in nums[::-1]:
            aft.append(aft[-1]*i)
        # aft=aft[::-1][:len(nums)]
        # bef=bef[1:]
        result=[]
        aft=aft[::-1]
        for i in range(len(nums)):
            val=bef[i]*aft[i+1]
            result.append(val)
        print(result)
        print(aft , bef)
        return result
        