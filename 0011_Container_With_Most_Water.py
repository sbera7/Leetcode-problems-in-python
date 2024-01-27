class Solution:
    def maxArea(self, height: list[int]) -> int:
        right_pointer = len(height) - 1
        left_pointer = 0
        max_area = 0
        for i in height:
            area = (right_pointer - left_pointer) * min(height[left_pointer], height[right_pointer])
            if area > max_area: max_area = area
            if height[left_pointer] < height[right_pointer]: left_pointer = left_pointer + 1
            else: right_pointer = right_pointer - 1
            if left_pointer > right_pointer:
                break
        return max_area
