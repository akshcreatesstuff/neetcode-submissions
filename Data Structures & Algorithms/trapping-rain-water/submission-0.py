class Solution:
    def trap(self, height: List[int]) -> int:
        max_water = 0
        n = len(height)
        l, r = 0, n - 1
        l_max = height[l]
        r_max = height[r]
        while l < r:
                if l_max < r_max:
                    l += 1
                    l_max = max(l_max, height[l])
                    max_water += l_max - height[l]
                else:
                    r -= 1
                    r_max = max(r_max, height[r])
                    max_water += r_max - height[r]
                
        return max_water


        