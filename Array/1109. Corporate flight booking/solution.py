class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        if n <= 0:
            return None
        
        diff = [0 for _ in range(n+1)]
        for booking in bookings:
            diff[booking[0]] += booking[2]
            if booking[1] + 1 < n+1:
                diff[booking[1]+1] -= booking[2]
        
        answer = [0 for _ in range(n)]
        answer[0] = diff[1]
        for i in range(1, n):
            answer[i] = answer[i-1] + diff[i+1]
        
        return answer