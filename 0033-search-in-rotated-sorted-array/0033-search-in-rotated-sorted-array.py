class Solution:
    def search(self, num: List[int], target: int) -> int:
        beg=0
        end=len(num)-1
        while beg<=end:
            mid=(beg+end) // 2
            if num[mid]==target:
                return mid
            if num[mid] >= num[beg]:
                if num[mid] >= target and target >=num[beg]:
                    end=mid-1
                else:
                    beg=mid+1
            else:
                if num[mid] <= target and target <= num[end]:
                    beg=mid+1
                else:
                    end=mid-1
        return -1 if num[end] != target else end

                    