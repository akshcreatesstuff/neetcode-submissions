class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cmap = {}
        max_len = 0

        left = 0

        for right, c in enumerate(s):
            if c in cmap and cmap[c] >= left:
                left = cmap[c] + 1
            
            cmap[c] = right
            max_len = max(max_len, right - left + 1)
        return max_len
        