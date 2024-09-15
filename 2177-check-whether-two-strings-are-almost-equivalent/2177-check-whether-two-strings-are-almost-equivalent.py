class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cnt1=Counter(word1)
        cnt2=Counter(word2)
        for key , value in cnt1.items():
            val=cnt2[key]
            if val != None and abs(val-value)>3:
                return False
        for key , value in cnt2.items():
            val=cnt1[key]
            if val != None and abs(val-value)>3:
                return False
        return True