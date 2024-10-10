class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left=sum(cardPoints[:(len(cardPoints)-k)])
        right=sum(cardPoints[len(cardPoints)-k:])
        print(left , right)
        maxima=right
        l=0
        print(len(cardPoints)-k  , len(cardPoints))
        for i in range(len(cardPoints)-k, len(cardPoints)):
            right+=cardPoints[l]
            right-=cardPoints[i]
            l+=1
            maxima=max(maxima , right)
        return maxima