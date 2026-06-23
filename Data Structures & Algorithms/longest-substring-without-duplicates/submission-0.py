class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        dupes = set()
        left = 0  
        longest = 0
        for right in range(n):
            while s[right] in dupes:
                dupes.remove(s[left])  
                left += 1
            dupes.add(s[right])  
            longest = max(longest, right - left + 1)
        return longest

        