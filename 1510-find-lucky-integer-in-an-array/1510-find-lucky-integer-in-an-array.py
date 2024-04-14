class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky={}
        for i in arr:
            if i in lucky:
                lucky[i]+=1
            else:
                lucky[i]=1
        result=-1
        for num , freq in lucky.items():
            if num == freq:
               result=max(result, num)
        return result