class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """

        diff = [0 for _ in range(1001)]
        for trip in trips:
            diff[trip[1]] += trip[0]
            if trip[2] < 1001:
                diff[trip[2]] -= trip[0]

        output = [capacity for _ in range(1001)]
        output[0] -= diff[0]
        if output[0] < 0:
            return False
        for i in range(1, 1001):
            output[i] = output[i-1] - diff[i]
            if output[i] < 0:
                return False
        
        return True
