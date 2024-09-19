class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res=[]
        count=0
        for i in words:
            res.append(''.join(sorted(set(i))))
        for i in range(len(res)):
            for j in range(i+1 , len(res)):
                if res[i]==res[j]:
                    count+=1


           
        return count