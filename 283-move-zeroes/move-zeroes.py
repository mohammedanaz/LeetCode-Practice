class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 0:
                count += 1
                nums.remove( nums[i])
                n -= 1
            else:
                i += 1
        zeros = [0] * count 
        nums.extend(zeros)
        