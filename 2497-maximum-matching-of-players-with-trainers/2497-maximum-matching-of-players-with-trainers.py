class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        l=r=cnt=0
        while l<len(players) and r<len(trainers):
            if players[l]<=trainers[r]:
                l+=1
                cnt+=1
            r+=1
        return cnt