class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result=[0]*n
        for i in range(len(bookings)):
            x , y , z =bookings[i]
            result[x-1]+=z
            if (y-1)+1 < len(result):
                result[(y-1)+1]-=z
        sums=0
        res=[]
        for i in range(len(result)):
            sums+=result[i]
            res.append(sums)
        return res