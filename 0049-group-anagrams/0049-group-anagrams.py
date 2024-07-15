class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hsh={}
        for i in strs:
            strs=''.join(sorted(i))
            
            if strs in hsh:
                hsh[strs].append(i)
            else:
                hsh[strs]=[i]
        result=[]
        print(hsh)
        for key , value in hsh.items():
            result.append(value)
        return result
        