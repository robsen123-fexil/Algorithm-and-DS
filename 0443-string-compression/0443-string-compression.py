class Solution:
    def compress(self, chars: List[str]) -> int:
        r =l=0
        while r<len(chars):
            count=0
            char=chars[r]
            while r<len(chars) and chars[r]==char:
                count+=1
                r+=1
            chars[l]=char
            l+=1
            if count>1:

                for val in str(count):
                    chars[l]=val
                    l+=1
            
            
        return l

        