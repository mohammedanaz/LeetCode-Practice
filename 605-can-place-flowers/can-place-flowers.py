class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new_plots = 0
        length = len(flowerbed)
        i = 0
        while i < length:
            if flowerbed[i] == 0:
                if (i==0 or flowerbed[i-1]==0) and (i==length-1 or flowerbed[i+1]==0):
                    flowerbed[i] = 1
                    new_plots += 1
                    if new_plots >= n:
                        return True
                    i += 2
                else:
                    i += 1
            else:
                i += 1
        return new_plots >= n
        