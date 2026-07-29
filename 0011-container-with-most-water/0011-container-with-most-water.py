class Solution(object):
    def maxArea(self, height):
        """ 
        # Brute Force
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res
        """

        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res

        