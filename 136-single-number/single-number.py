class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        actual_sum = sum(nums)
        nums[:] = set(nums)
        unique_sum = sum(nums)
        return 2*unique_sum - actual_sum
        