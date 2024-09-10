class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=Counter(nums)
        half=len(nums)//2
        cnt=dict(sorted(cnt.items() , key=lambda x:x[1] , reverse=True))
        for key , value in cnt.items():
            if value >=half:
                return key