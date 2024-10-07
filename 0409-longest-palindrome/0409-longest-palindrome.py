class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt=Counter()
        count=0
        for i in range(len(s)):
            cnt[s[i]]+=1
            if cnt[s[i]]%2==0:
                count+=2
        print(count)
        for i in cnt.values():
            if i%2!=0:
                count+=1
                break
        return count