class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_count={}
        for i in stones:
            if i in stone_count:
                stone_count[i]+=1
            else:
                stone_count[i]=1
        jew=0
        for i in jewels:
            if i in stone_count:
                jew+=stone_count[i]
        return jew