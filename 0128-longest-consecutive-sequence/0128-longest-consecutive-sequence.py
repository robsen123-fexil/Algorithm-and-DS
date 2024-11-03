class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets=set(nums)
        longest=0
        print(sets)
        for i in sets:
            if (i-1) not in sets:
                print(i-1)
                leng=1
                while i+leng in sets:
                    leng+=1
                longest=max(leng , longest)
        return longest