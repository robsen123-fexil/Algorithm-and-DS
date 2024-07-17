class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target_unicode=ord(target)-ord('a')
        for i in letters:
            letter_unicode=ord(i)-ord('a')
            if target_unicode<letter_unicode:
                return i
        else:
            return letters[0]