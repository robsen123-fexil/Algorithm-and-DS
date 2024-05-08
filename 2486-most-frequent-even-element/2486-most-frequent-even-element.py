class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # hashmap={}
        # res=[]
        # for i in nums:
        #     if i in hashmap:
        #         hashmap[i]+=1
        #     else:
        #         hashmap[i]=1
        # result={}
        # res=sorted(hashmap.items() , key = lambda item:(item[1])  , reverse=True)
        # resu={ k : v for k , v in res }
        # for key , value in res:
        #     if key%2==0:
        #         return key
        
        
        # return -1
        # count=Counter(nums)
        # res={k : v for k ,  v in count.items() if k%2==0}
        
        # if res:
        #     return max(res , key = res.get)
        # else:
        #     return -1
        count=Counter(nums)
        result=[num for num in count if num%2==0]
        if not result:
            return -1
        maxima=max(result , key =lambda x:(count[x] , -x))
        return maxima

        
       
        
        