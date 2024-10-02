class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left=[]
        right=[]
        for i in nums:
            if i%2==0:
                left.append(i)
            else:
                right.append(i)
        return left+right
