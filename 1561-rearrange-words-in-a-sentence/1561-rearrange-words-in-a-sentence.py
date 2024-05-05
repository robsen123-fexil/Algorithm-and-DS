class Solution:
    def arrangeWords(self, text: str) -> str:
        result=[]
        res=text.split()
        for i in res:
            result.append(i.lower())
        return " ".join(sorted(result , key=len)).capitalize()
        