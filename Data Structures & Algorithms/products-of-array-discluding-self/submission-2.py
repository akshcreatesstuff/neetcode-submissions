class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for curr_idx in range(n):
            i = 0
            prod = 1
            while i < n:
                if i != curr_idx:
                    prod = prod * nums[i]
                i += 1      
            ans.append(prod)
        return ans
        