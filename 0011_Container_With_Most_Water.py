class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        while left <= right:
            if min(height[left], height[right]) * (right - left) > area: area = min(height[left], height[right]) * (right - left)
            if height[left] > height[right]: right -= 1
            else: left += 1
        return area
