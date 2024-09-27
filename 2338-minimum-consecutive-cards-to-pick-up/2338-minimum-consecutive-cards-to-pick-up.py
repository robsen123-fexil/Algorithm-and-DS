class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hsh={}
        maxima=float('inf')
        for i in range(len(cards)):
            if cards[i] in hsh:
                maxima=min(maxima , i-hsh[cards[i]]+1)
            hsh[cards[i]]=i
        return maxima if maxima!=float('inf') else -1
                