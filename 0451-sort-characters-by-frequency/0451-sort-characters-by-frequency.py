class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        strs=""
        ss=dict(sorted(count.items() , key=lambda x:x[1] , reverse=True))
        for key , value in ss.items():
            strs+=(key)*value
        return strs