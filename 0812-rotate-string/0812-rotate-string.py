class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        sh=s+s
        if goal in sh:
            return True
        return False