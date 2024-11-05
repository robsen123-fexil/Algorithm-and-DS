class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        hsh={}
        for i in range(len(numbers)):
            if target-numbers[i] in hsh:
                return [hsh[target-numbers[i]]+1 , i+1]
            if numbers[i] not in hsh:
                hsh[numbers[i]]=i
        
        