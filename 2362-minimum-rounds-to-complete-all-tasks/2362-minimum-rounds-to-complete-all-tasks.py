class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt=Counter(tasks)
        count=0
        for val in cnt.values():
            if val<2:
                return -1
            if val%3==0:
                count+=(val//3)
            elif val==2:
                count+=(1)
            else:
                count+=(val//3)+1
        return count