class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        copied_elements = []
        k = 0
        for i in range(len(nums)):
            if nums[i] not in copied_elements:
                nums[k] = nums[i]
                copied_elements.append(nums[i])
                k += 1
        return k
