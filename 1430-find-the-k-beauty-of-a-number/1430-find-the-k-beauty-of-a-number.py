class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        str_num=str(num)
        count=0
        for i in range(len(str_num)-k+1):
            sub_str=str_num[i:i+k]
            diviser=int(sub_str)
            if diviser !=0 and num%diviser==0:
                count+=1
        return count
