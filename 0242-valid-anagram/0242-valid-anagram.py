class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts=Counter(s)
        countt=Counter(t)
        sorts=sorted(counts.items() , key=lambda x:x[0])
        sort = sorted(countt.items() , key = lambda x:x[0])
        return sort==sorts

            
                    