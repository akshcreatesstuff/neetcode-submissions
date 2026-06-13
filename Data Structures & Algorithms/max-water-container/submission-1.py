class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        longest = 0
        for i in range(n):
            for j in range(i + 1, n):
                area = min(heights[i], heights[j]) * (j - i)
                longest = max(longest, area)
        return longest
        