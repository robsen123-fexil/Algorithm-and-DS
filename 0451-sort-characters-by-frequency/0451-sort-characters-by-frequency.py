class Solution:
    def frequencySort(self, s: str) -> str:
        strs=""
        cnt=Counter(s)
        cnt=dict(sorted(cnt.items() , key=lambda x:x[1] , reverse=True))
        for key , value in cnt.items():
            for i in range(value):
                strs+=key
        return strs