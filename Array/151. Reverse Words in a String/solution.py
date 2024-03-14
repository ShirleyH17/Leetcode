class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Removing leading and trailing blank spaces
        left = 0
        right = len(s) - 1
        while left <= right and s[left] == " ":
            left += 1
        while right >= left and s[right] == " ":
            right -= 1
        s = s[left:right+1]

        # Split the processed string into words
        words = s.split()
        
        output = words[-1]
        if len(words) == 1:
            return output
        for i in range(len(words)-2, -1, -1):
            output = output + " " + words[i]
        return output
        # Python string immutable
        # If mutable, can first reverse the string, then reverse each word


