class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.append(target)
        letters.sort()
        
        sets=sorted(list(set(letters)))
        ind=sets.index(target)
        print(sets , ind)
        if ind+1<len(sets):
            print("sjs")
            return sets[ind+1]
        else:
            return sets[0]