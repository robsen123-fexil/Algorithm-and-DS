class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        list_num=[int(i) for i in nums]
        list_num.sort()
        num=list_num[::-1]
        return str(num[k-1])
