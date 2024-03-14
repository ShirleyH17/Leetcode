# Solution 1
# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         left = 0
#         right = len(nums) - 1

#         while left <= right:
#             middle = (left + right) // 2
#             if nums[middle] > target:
#                 right = middle - 1
#             elif nums[middle] < target:
#                 left = middle + 1
#             else:
#                 return middle
        
#         if nums[middle] < target:
#             return middle + 1
#         else:
#             return middle


# Solution 2
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.findLeftBound(nums, target), self.findRightBound(nums, target)]


    def findLeftBound(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] >= target:
                right = middle - 1
            else:
                left = middle + 1
        
        # When left exceeds the length of array or right exceeds the length of array
        if left > len(nums) - 1 or nums[left] != target:
            return -1

        return left


    def findRightBound(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        
        # When left exceeds the length of array or right exceeds the length of array
        if right < 0 or nums[right] != target:
            return -1

        return right
