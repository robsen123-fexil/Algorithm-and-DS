class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        dic=sorted(dic.items() , key=lambda x:x[1] , reverse=True)
        res=[]
        print(dic)
        for key , value in dic:
            res.append(value) 
            break 
        count=0
        print(res)
        for key , value in dic:
            if value in res:
                count+=value
        return count


