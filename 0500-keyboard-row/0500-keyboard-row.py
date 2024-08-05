class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        hsh={'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1,'o': 1 ,'p':1,'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2,'l': 2,'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3}
        result=[]
        for i in words:
            stack=[]
            for j in i:
                val=hsh.get(j.lower())
                if stack:
                    if stack[-1]==val:
                        stack.append(val)
                    else:
                        break
                else:
                    stack.append(val)
            if len(stack)==len(i):
                result.append(i)
        return result
            



        
        
        