class Solution:
    def minimumDeletions(self, s: str) -> int:
        count=0
        a='a'
        b='b'
        stack=[]
        for i in s:
            if stack and i==a and stack[-1]==b:
                count+=1
                stack.pop()
            else:

                stack.append(i)
        return count
