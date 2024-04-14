class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height)-1
        max_left, max_right = height[left], height[right]
        water_contains = 0

        while(left < right):
            # print(left, right, water_contains)
            if max_left <= max_right:
                left += 1
                water_contains += self.is_positive(min(max_left, max_right) - height[left])  # current
                max_left = max(max_left, height[left])
            else:
                right -= 1
                water_contains += self.is_positive(min(max_left, max_right) - height[right]) # current
                max_right = max(max_right, height[right])

        return water_contains

    def is_positive(self, num):
        return num if num > 0 else 0