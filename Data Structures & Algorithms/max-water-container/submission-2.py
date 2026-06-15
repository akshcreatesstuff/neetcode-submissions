class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # n = len(heights)
        # longest = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         area = min(heights[i], heights[j]) * (j - i)
        #         longest = max(longest, area)
        # return longest



        n = len(heights)
        left = 0
        right = n - 1
        maxArea = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left) 
            maxArea = max(area, maxArea)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea

        