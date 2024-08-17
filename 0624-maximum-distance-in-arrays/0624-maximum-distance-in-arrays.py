class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        curmin=arrays[0][0]
        curmax=arrays[0][-1]
        maxi=float('-inf')
        for i in range(1 , len(arrays)):
            imin=arrays[i][0]
            imax=arrays[i][-1]
            maxi=max(maxi , abs(curmax-imin)  , abs(imax-curmin))
            curmax=max(curmax , imax)
            curmin=min(curmin , imin)
        return maxi