class Solution:
    def compress(self, chars: List[str]) -> int:
        r=0
        l=0
        while r<len(chars):
            count=0
            strt=chars[r]
            while r<len(chars) and chars[r]==strt:
                count+=1
                r+=1
            chars[l]=strt
            l+=1
            if count>1:
                for i in str(count):
                    chars[l]=i
                    l+=1
        return l
