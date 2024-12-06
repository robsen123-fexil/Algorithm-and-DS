class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        nums=[]
        banned=set(banned)
        for i in range(1 , n+1):
            if i not in banned:
                nums.append(i)
        maxima=0
        sums=0
        for i in range(len(nums)):
            sums+=nums[i]
            if sums<=maxSum:
                maxima+=1
            else:
                break
        return maxima