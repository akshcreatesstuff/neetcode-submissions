class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set(nums)
        n = len(nums)
        ans = 0
        for num in nums:
            if num - 1 not in count:
                curr = num
                length = 1
            
                while curr + 1 in count:
                    length += 1
                    curr += 1
                ans = max(ans, length)
        return ans



      



        