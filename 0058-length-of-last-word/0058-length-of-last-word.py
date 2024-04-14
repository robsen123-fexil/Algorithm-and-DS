class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r=s.split()
        re=r[-1]
        count =0
        for i in  re:
            count+=1
        return count    