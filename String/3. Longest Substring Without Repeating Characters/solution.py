class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        window = defaultdict(int)

        left, right = 0, 0
        length = 0

        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            
            # notice that when window[d] -= 1, the element was not removed from the dict
            while right - left > len(window):
                d = s[left]
                left += 1
                window[d] -= 1
                if window[d] == 0:
                    del window[d]
            
            length = max(right - left, length)
        
        return length
