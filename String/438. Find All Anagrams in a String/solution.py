class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        output = []
        from collections import defaultdict
        target, window = defaultdict(int), defaultdict(int)
        for char in p:
            target[char] += 1
        
        left, right = 0, 0
        valid = 0
        while right < len(s):
            c = s[right]
            right += 1
            if c in target:
                window[c] += 1
                if window[c] == target[c]:
                    valid += 1

            while valid == len(target):
                if right - left == len(p):
                    output.append(left)
                d = s[left]
                left += 1
                if d in window:
                    if window[d] == target[d]:
                        valid -= 1
                    window[d] -= 1
        
        return output