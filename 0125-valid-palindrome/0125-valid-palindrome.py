class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs=""
        for i in s:
            if i.isalpha() or i.isdigit():
                strs+=i.lower()
            
        return strs==strs[::-1]