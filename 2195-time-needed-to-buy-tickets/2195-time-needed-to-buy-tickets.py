class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        que=deque()
        for i in range(len(tickets)):
            que.append([i , tickets[i]])
        count=0
        while que:

            val=que.popleft()
            x , y = val
            count+=1
            if y-1 ==0 and x==k:
                return count
            elif y-1!=0:
                que.append([x , y-1])
        return count
                

            

        return count