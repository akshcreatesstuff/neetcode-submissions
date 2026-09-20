class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        c_map = {}

        for right, c in enumerate(s):
            if c in c_map and c_map[c] >= left:
                left = c_map[c] + 1

            c_map[c] = right
            max_len = max(max_len, right - left + 1)
        return max_len

        