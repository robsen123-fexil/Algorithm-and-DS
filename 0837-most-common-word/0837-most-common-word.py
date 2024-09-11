class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punc=[',' , '!' , '?' , "'" , ';' , '.']
        strs=""
        for i in range(len(paragraph)):
            if paragraph[i] in punc:
                strs+=' '
            else:
                strs+=paragraph[i].lower()
        strs=strs.split()
        cnt=Counter(strs)
        res=defaultdict(list)
        for key , value in cnt.items():
            if key not in banned:
                res[key]=value
        maxima=max(res , key = res.get)
        print(strs)
        strs
        return maxima