class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        temp_len = 0
        for num in s:
            if num - 1 not in s:
                curr = num
                temp_len = 1
                while curr + 1 in s:
                    curr += 1
                    temp_len += 1
                ans = max(ans, temp_len)
        return ans

  

        