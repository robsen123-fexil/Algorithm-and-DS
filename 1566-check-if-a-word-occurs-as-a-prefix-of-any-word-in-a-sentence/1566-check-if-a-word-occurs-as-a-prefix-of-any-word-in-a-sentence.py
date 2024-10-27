class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        strs=sentence.split()
        for i in range(len(strs)):
            l=0
            r=0
            while l<len(strs[i]) and r<len(searchWord):
                if strs[i][l]==searchWord[r]:
                    r+=1
                l+=1
                if l!=r:
                    break
            if len(searchWord)==r:
                return i+1
        return -1
        

        
            