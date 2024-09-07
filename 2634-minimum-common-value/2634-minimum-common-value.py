class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        hsh={}
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        for i in nums1:
            if i not in hsh:
                hsh[i]=1
            else:
                hsh[i]+=1
        for j in nums2:
            if j not in hsh:
                hsh[j]=1
            else:
                hsh[j]+=1
                
        result=[]
        for key , value in hsh.items():
            if value>=2:
                result.append(key)
        if result:
            return min(result)
        else:
            return -1

