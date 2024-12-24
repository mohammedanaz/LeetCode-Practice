class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        result = []
        largest_num = max(candies)
        print(largest_num)
        for x in candies:
            diff = largest_num - x
            if diff > extraCandies:
                result.append(False)
            else:
                result.append(True)
        return result