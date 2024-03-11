class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return len(nums)
        
        fast, slow, temp = 1, 0, 1
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                temp += 1
                if temp < 3:
                    slow += 1
                    nums[slow] = nums[fast]
                fast += 1
            else:
                temp = 1
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        
        return slow + 1

