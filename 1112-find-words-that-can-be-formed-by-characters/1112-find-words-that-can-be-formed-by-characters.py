class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt=Counter(chars)
        count=0
        for i in words:
            cnt1=Counter(i)
            l=0
            for key , value in cnt1.items():
                if key in cnt and cnt[key]>=value:
                    l+=1
                else:
                    break
            if l==len(cnt1):
                count+=(len(i))
        
        return count       
                
