class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        l = r = 0
        w1 = list(word1)
        w2 = list(word2)
        result = ""
        
        while l < len(w1) and r < len(w2):
            if w1[l] > w2[r]:
                result += w1[l]
                l += 1
            elif w2[r] > w1[l]:
                result += w2[r]
                r += 1
            else:
                # Compare one by one manually
                temp_l = l
                temp_r = r
                while temp_l < len(w1) and temp_r < len(w2):
                    if w1[temp_l] > w2[temp_r]:
                        result += w1[l]
                        l += 1
                        break
                    elif w1[temp_l] < w2[temp_r]:
                        result += w2[r]
                        r += 1
                        break
                    temp_l += 1
                    temp_r += 1
                
                # If we reach the end of one string and still no difference, take from the longer one
                if temp_l == len(w1):
                    result += w2[r]
                    r += 1
                elif temp_r == len(w2):
                    result += w1[l]
                    l += 1
        
        # Append any remaining characters from word1 or word2
        while l < len(w1):
            result += w1[l]
            l += 1
        
        while r < len(w2):
            result += w2[r]
            r += 1
        
        return result
