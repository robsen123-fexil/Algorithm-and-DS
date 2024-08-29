class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=list(version1.split('.'))
        version2=list((version2.split('.')))
        print(version1 , version2)
        
        
        for ind , (i , j) in enumerate(zip(version1  , version2)):
            
            if int(i)> int(j):
                return 1
            elif int(i)<int(j):
                print("here")
                return -1
            else:
                continue
        print(ind)
        if len(version1)>len(version2):
            for ind in range(len(version2) , len(version1)):
                if int(version1[ind])>0:
                    return 1
        elif len(version1)<len(version2):
            for ind in range(len(version1) ,len(version2)):
                if int(version2[ind])>0:
                    return -1
       
        return 0
