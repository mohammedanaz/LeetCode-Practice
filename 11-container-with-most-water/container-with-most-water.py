class Solution:
    def maxArea(self, height: List[int]) -> int:
        right = len(height) - 1
        left = 0
        area = 0
        while left < right:
            left_h = height[left]
            right_h = height[right]
            x = right - left
            y = min(left_h, right_h)
            area = max(area, x * y)
            if left_h <= right_h:
                left += 1
            else:
                right -= 1
        return area
                    