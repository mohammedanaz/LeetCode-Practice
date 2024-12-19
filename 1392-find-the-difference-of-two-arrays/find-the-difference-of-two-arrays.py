class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        joined_lst = list(set(nums1 + nums2))
        l1 = []
        l2 = []
        for x in joined_lst:
            if x in nums1 and x in nums2:
                continue
            elif x in nums1:
                l1.append(x)
            else:
                l2.append(x)
        return [l1, l2]