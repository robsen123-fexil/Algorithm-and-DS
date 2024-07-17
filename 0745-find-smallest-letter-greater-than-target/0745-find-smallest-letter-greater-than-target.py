class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low=0
        high=len(letters)-1
        for i in letters:
            if i>target:
                return i
        else:
            return letters[0]

        