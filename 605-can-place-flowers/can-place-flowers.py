class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new_plots = 0
        length = len(flowerbed)
        i = 0
        for i in range(length):
            if flowerbed[i] == 0:
                prev = i == 0 or flowerbed[i - 1] == 0
                next = i == length - 1 or flowerbed[i + 1] == 0
                if prev and next:
                    new_plots += 1
                    flowerbed[i] = 1
                    if new_plots >= n:
                        return True
        return new_plots >= n
        