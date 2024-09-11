class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split()
        s2=s2.split()
        s3=s1+s2
        cnt=Counter(s3)
        result=[]
        for key , value in cnt.items():
            if value ==1:
                result.append(key)
        
        return result