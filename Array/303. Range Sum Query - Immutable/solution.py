class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = nums

        def sum(nums):
            sum = []
            total = 0
            for number in nums:
                total += number
                sum.append(total)
            return sum
        
        self.total = sum(self.arr)


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.total[right]
        return self.total[right] - self.total[left-1]
        
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)