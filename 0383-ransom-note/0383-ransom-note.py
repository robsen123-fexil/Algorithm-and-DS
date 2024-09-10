class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l=r=0
        ransomNote=sorted(list(ransomNote))
        magazine=sorted(list(magazine))
        while l<len(ransomNote) and r<len(magazine):
            while r<len(magazine) and magazine[r]!=ransomNote[l]:
                
                r+=1
            if r<len(magazine) and magazine[r]==ransomNote[l]:
                l+=1
                r+=1
            
        return l==len(ransomNote)