class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k == 0 or len(nums) == 1:
            return nums
        
        actualTimes = k % len(nums)
        # Reverse the array
        self.reverse(nums, 0, len(nums)-actualTimes-1)
        self.reverse(nums, len(nums)-actualTimes, len(nums)-1)
        self.reverse(nums, 0, len(nums)-1)
        return nums

    
    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1