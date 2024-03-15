class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""
        
        # if key does not exist in the dict, will return default value 0 in this case
        from collections import defaultdict
        target, window = defaultdict(int), defaultdict(int)

        for char in t:
            target[char] += 1
        
        left, right = 0, 0
        valid = 0
        start, length = 0, float("inf")
        while right < len(s):
            c = s[right]
            right += 1
            if c in target:
                window[c] += 1
                if window[c] == target[c]:
                    valid += 1
            
            while valid == len(target):
                if right - left < length:
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                if d in target:
                    if window[d] == target[d]:
                        valid -= 1
                    window[d] -= 1
                
        return "" if length == float("inf") else s[start:start + length]