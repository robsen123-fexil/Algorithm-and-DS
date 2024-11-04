class Solution:
    def compressedString(self, word: str) -> str:
        cnt=Counter()
        comp=""
        l=0
        r=0
        while r<len(word):
            strs=""
            while r<len(word) and word[r]==word[l]:
                strs+=word[r]
                r+=1
            l=r
            
            cnt=Counter(strs)
            for key , val in cnt.items():
                if val<=9:
                    comp+=str(val)
                    comp+=key
                else:
                    while val>9:
                        comp+=str(9)
                        comp+=key
                        val-=9
                    comp+=str(val)
                    comp+=key
        return comp
                

