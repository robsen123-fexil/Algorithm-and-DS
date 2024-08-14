class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap1={}
        # for num in nums:
        #     if num in hashmap1:
        #         hashmap1[num]+=1
        #     else:
        #         hashmap1[num]=1
        # val=sorted(hashmap1.items(), key=lambda x:x[1])
        # if len(val)>=k:
        #     ans=[key for key, _ in val[-k:]]
        # else:
        #     ans=[key for key, _ in val]
        # return ans
        # hashmap1={}
        # for i in nums:
        #     if i in hashmap1:
        #         hashmap1[i]+=1
        #     else:
        #         hashmap1[i]=1
        # val =sorted(hashmap1.items() , key =lambda x:x[1])
        # ans=[]
        # if len(val)>=k:
        #     ans=[key for key , _ in val[-k:]]
        # else:
        #     ans=[key for key, _ in val]
        # return ans
        count=Counter(nums)
        count=dict(sorted(count.items() , key =lambda x:x[1] ,  reverse=True) ,)
        print(count)
        result=[]
        l=0
        sol=[]
        for key , value in count.items():
            result.append(key)
        while k>0:
            sol.append(result[l])
            l+=1
            k-=1

        return sol


        result=[]
        
