class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        def checker(leng , word , searchword):
            res=list(word[:leng])
            
            if ''.join(res)==searchword:
                return True
            # l=0
            # for i in range(leng , len(word)):
            #     res.append(word[i])
            #     res.remove(word[l])
            #     if ''.join(res)==searchword:
            #         return True
            #     l+=1
            return False
        sent=sentence.split()
        for i in range(len(sent)):
            if checker(len(searchWord) ,sent[i] ,searchWord):
                return i+1
        return -1

        
