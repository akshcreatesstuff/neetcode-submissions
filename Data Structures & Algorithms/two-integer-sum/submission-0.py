class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(0, len(nums)):
            res = target - nums[i]
            if res in s:
                return [s[res], i]
            s[nums[i]] = i
        