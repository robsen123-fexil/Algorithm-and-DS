class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hsh={}
        for i  , value in enumerate(heights):
            hsh[value]=names[i]
        print(hsh)
        hsh=sorted(hsh.items() , reverse=True)
        print(hsh)
        resu=[]
        for i , key in hsh:
            resu.append(key)
        return resu