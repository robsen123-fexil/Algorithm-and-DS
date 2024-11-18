class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0]*len(code)
        elif  k>0:
            result=[]
            for i in range(len(code)):
                l=1
                count=1
                sums=0
                while count<=k:
                    val=i+l
                    if val <len(code):
                       
                        sums+=code[val]
                    else:
                        
                        sums+=code[val-len(code)]
                    count+=1
                    l+=1
                result.append(sums)
            return result
        elif k<0:
            print("helr")
            result=[]
            for i in range(len(code)):
                l=1
                count=1
                sums=0
                while count<=(k*-1):
                    val=i-l
                    sums+=code[val]
                    count+=1
                    l+=1
                result.append(sums)
            return result
