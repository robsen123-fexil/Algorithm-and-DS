class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        hsh={}
        for i in range(len(intervals)):
            a , b = intervals[i]
            hsh[a]=i
        srt=sorted(intervals , key=lambda x:[x[0]])
        cnt={}
        for i in range(len(srt)):
            a , b = srt[i]
            l=i+1
            if a>=b:
                cnt[a]=hsh[a]
                
            else:
                

                while l<len(srt):
                    x , y =srt[l]
                    if b<=x:
                      cnt[a]=hsh[x]
                      break
                    l+=1
                if l==len(srt):
                   cnt[a]=-1
        result=[]
        print(cnt)
        for i in intervals:
            a , b = i
            result.append(cnt[a])
        return result
        

                