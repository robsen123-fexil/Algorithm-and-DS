class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # result=[0]*(n+1)
        # for i in bookings:
        #     j , k , l =i
        #     result[j]+=l
        #     if k+1 < len(result):
        #         result[k+1]-=l
        # sums=0
        # for i in range(1 , len(result)):
        #     sums+=result[i]
        #     result[i]=sums
        # return result[1:]
        result=[0]*(n+1)
        for i in range(len(bookings)):
            x , y , z=bookings[i]
            result[x]+=z
            if (y+1)<len(result):
                result[y+1]-=z
        sums=0
        for i in range( len(result)):
            sums+=result[i]
            result[i]=sums
        return result[1:]
            
            