class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits)))
        num += 1
        nums = list(map(int, str(num)))
        return nums