class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt=Counter(tasks)
        for val in cnt.values():
            if val==1:
                return -1
        count=0
        upper=[]
        for key , value in cnt.items():
            if value == 3 or value == 2:
                count+=1
            else:
                upper.append([])
                for i in range(value):
                    upper[-1].append(key)
        print(count , upper)
        
        if upper:
            for i in upper:
                cnt=Counter(i)
                print(cnt)
                for key , value in cnt.items():
                    if value%3==0:
                        count+=(value//3)
                    else:
                        count+=(value//3)+1      
        return count
                        
    
            