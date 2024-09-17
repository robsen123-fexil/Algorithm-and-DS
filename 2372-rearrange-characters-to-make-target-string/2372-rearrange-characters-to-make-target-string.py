class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        cntt=Counter(target)
        cnts=Counter(s)
        minima=float('inf')
        for key , value in cntt.items():
            val=cnts[key]
            if val==0:
                return 0

            if value>val:
                return 0
            print(val , value)
            mini=min(val , value)
            maxi=max(val , value)
            valu=maxi//mini
            minima=min(minima , valu)
        return minima

