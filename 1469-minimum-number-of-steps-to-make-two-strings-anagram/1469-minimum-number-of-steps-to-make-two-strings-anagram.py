class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts=Counter(s)
        countt=Counter(t)
        count=0
        for keys , values in countt.items():
            val=counts.get(keys)
            if val==None:
                val=0
            if values>val:
                count+=abs(values-val)
            
        return count