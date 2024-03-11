# Solution 1
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numberOfElements = {}
        for num in nums:
            if str(num) not in numberOfElements:
                numberOfElements[str(num)] = 1
            else:
                numberOfElements[str(num)] += 1
        
        targetTimes = len(nums) // 2
        majorityElement = nums[0]
        for key in numberOfElements:
            if numberOfElements[key] > targetTimes + 1:
                return int(key)
            elif numberOfElements[key] > targetTimes:
                if numberOfElements[key] > numberOfElements[str(majorityElement)]:
                    majorityElement = key
        return int(majorityElement)

# Solution 2
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Moore's voting algorithm
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            
            if candidate == num:
                count += 1
            else:
                count -= 1
        
        return candidate