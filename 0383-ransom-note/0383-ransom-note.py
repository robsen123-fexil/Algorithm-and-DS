class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hsh1=Counter(ransomNote)
        hsh2=Counter(magazine)
        for key , value in hsh1.items():
            if key not in hsh2 or value > hsh2[key]:
                return False
        return True

             