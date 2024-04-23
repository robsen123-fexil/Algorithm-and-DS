class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        mat=list()
        neg=[]
        pos=[]
        for num in nums:
            if num <0:
                neg.append(num)
            if num>0:
                pos.append(num)
        return max(len(pos), len(neg))

        