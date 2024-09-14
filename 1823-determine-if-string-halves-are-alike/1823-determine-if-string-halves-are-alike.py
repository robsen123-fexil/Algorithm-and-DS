class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=list(s)
        left=s[len(s)//2:]
        vowels='aeiouAIEOU'
        right=s[:len(s)//2]
        cnt=Counter(left)
        cnt2=Counter(right)
        count1=count2=0
        for key , value in cnt.items():
            if key in vowels:
                count1+=value
        for key , value in cnt2.items():
            if key in vowels:
                count2+=value
        return count1==count2
