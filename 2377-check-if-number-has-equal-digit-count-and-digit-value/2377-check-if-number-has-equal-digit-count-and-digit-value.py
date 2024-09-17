class Solution:
    def digitCount(self, num: str) -> bool:
        hsh={}
        nums=[]
        for i in num:
            nums.append(int(i))
        for i , val in enumerate(nums):
            
            hsh[i]=val
        print(hsh)
        cnt=Counter(nums)
        print(cnt)
        for key , val in cnt.items():
            if key in hsh:

               value=hsh[key]
               if val!=value:
                  return False
            else:
                return False
        return True
