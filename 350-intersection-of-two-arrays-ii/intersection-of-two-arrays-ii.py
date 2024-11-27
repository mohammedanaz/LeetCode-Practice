class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
    
    # Find the intersection by taking the minimum count of each element
        result = []
        for num in count1:
            if num in count2:
                result.extend([num] * min(count1[num], count2[num]))
    
        return result