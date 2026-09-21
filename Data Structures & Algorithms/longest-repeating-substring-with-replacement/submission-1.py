class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        max_len = 0
        cmap = {}
        for right, c in enumerate(s):
            cmap[c] = cmap.get(c,0) + 1
            max_len = max(max_len, cmap[c])
            
            while (right - left + 1) - max_len > k:
                cmap[s[left]] -= 1
                left += 1
            ans = max(max_len, right - left + 1)
        return ans
        