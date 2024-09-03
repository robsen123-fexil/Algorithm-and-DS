class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l=r=0
        v1=version1.split('.')
        v2=version2.split('.')
        print(v1 , v2)
        while l<len(v1) and r < len(v2):
            
            if int(v1[l])> int(v2[r]):
            
                return 1
            elif int(v1[l]) < int(v2[r]):
                return -1
            l+=1
            r+=1
        if l<(len(v1)):
            while l<len(v1):
                if int(v1[l])>0:
                    return 1
                l+=1
        if r<(len(v2)):
            while r<len(v2):
                if int(v2[r])>0:
                    return -1
                r+=1                    
        return 0
