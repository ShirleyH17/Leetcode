class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                leftmost, rightmost = middle, middle
                if middle - 1 >= 0 and nums[middle-1] == target:
                    leftmost = min(leftmost, left + self.searchRange(nums[left:middle], target)[0])
                if middle + 1 < len(nums) and nums[middle+1] == target:
                    rightmost = max(rightmost, middle + 1 + self.searchRange(nums[middle+1:right+1], target)[1])
                return [leftmost, rightmost]

        return [-1, -1]