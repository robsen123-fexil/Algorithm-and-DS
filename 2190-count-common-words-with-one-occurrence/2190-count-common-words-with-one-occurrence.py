class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt=Counter(words1)
        cnt2=Counter(words2)
        res=[]
        for key , val in cnt.items():
            if val==1:
                res.append(key)
        count=0
        for i in res:
            val=cnt2[i]
            if val==1:
                count+=1
        return count
