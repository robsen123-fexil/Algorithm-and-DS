class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt=Counter('balloon')
        cnt2=Counter(text)
        minima=float('inf')
        for key , val in cnt.items():
            if key not in cnt2:
                return 0
            else:
                values=cnt2[key]//val
                minima=min(minima , values)
        return minima if minima!=float('inf') else 0