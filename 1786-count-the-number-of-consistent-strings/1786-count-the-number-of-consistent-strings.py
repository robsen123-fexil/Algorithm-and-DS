class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        word=[]
        count=0
        for i in words:
            word.append(list(set(i)))
        cnt1=Counter(allowed)
        for i in word:
            cnt=list(set(i))
            l=0
            for j in i:
                if j not in cnt1:
                    break
                else:
                    l+=1
            if l==len(i):
                count+=1
        return count

            
            


        

