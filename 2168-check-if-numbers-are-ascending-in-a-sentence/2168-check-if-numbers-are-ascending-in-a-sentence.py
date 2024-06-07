class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        def checker(res , l , r):
            while r<len(res):
                if res[l]>=res[r]:
                    return False
                l+=1
                r+=1
            return True
            

            
        ss=s.split()
        res=[]
        for i in ss:
            if i.isdigit():
                res.append(int(i))
            else:
                for j in i:
                    if j.isdigit():
                        res.append(int(j))
                        break
        return checker(res, 0 , 1)
        
        