class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        l=0
        r=len(numbers)-1
        while l<r:
            res=numbers[r]+numbers[l]
            if res>target:
                r-=1
            elif res<target:
                l+=1
            else:
                return [l+1,r+1]

        return []
        