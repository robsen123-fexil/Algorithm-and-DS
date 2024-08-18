class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt=Counter()
        l=0
        maxima=float('-inf')
        for i in range(len(fruits)):
            cnt[fruits[i]]+=1
            while len(cnt)>2:
                cnt[fruits[l]]-=1
                if cnt[fruits[l]]==0:
                    cnt.pop(fruits[l])
                l+=1
            maxima=max(maxima  , i-l+1)
        return maxima if maxima!=float('-inf') else 0