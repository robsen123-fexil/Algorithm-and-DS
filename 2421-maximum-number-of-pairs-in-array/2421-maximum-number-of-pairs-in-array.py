class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt=Counter(nums)
        count=r=0
        res=[]
        print(cnt)
        for key , val in cnt.items():
            if val%2==0:
                print(key , val)
                count+=(val//2)
            else:
                count+=(val//2)
                r+=1
        
        res.append(count)
        res.append(r)
        return res