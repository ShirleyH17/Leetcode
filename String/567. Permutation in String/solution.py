class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Check whether there is a substring s in s2 such that len(s) == len(s1) and contains all elements in s1
        
        if len(s1) > len(s2):
            return False

        from collections import defaultdict
        target, window = defaultdict(int), defaultdict(int)
        for char in s1:
            target[char] += 1
        
        left, right = 0, 0
        valid = 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in target:
                window[c] += 1
                if window[c] == target[c]:
                    valid += 1
            
            while valid == len(target):
                if right - left == len(s1):
                    return True
                d = s2[left]
                left += 1
                if d in window:
                    if window[d] == target[d]:
                        valid -= 1
                    window[d] -= 1
            
        return False