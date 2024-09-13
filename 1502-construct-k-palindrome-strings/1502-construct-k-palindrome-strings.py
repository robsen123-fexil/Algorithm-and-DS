class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        cnt=Counter(s)
        print(cnt)
        count=0
        if len(s)<k:
            return False
        for key , value in cnt.items():
            if value%2!=0:
                count+=1
        print(count)
        if count>k:
            return False
        return True