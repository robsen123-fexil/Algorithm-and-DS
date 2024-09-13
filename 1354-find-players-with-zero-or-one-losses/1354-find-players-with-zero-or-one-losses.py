class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner=[]
        looser=[]
        for i in matches:
            x, y=i
            winner.append(x)
            looser.append(y)
        cntlooser=Counter(looser)
        cntlooser=defaultdict(int)
        for i in looser:
            cntlooser[i]+=1
        result=[]
        result.append(set())
        for i in winner:
            if cntlooser[i]==0:
                result[-1].add(i)
        result.append(set())
        for key , value in cntlooser.items():
            if value ==1:
                result[-1].add(key)
        sol=[]
        for i in result:
            sol.append(list(i))
        solu=[]
        for i in sol:
            solu.append(sorted(i))            
        return solu

        