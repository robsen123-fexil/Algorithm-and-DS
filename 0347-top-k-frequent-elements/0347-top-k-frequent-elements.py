class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt=Counter(nums)
        res=[]
        l=0
        print(cnt)
        cnt=dict(sorted(cnt.items() , key=lambda x:x[1]   , reverse=True))
        print(cnt)
        res=[k for k in cnt.keys()]
        print(res)
        return res[:k]
        


