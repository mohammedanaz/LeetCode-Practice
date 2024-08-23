class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close_sum = float('inf')
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1 , len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target:
                    return current_sum
                if abs(current_sum - target) < abs(close_sum - target):
                    close_sum = current_sum
                if current_sum < target:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return close_sum 