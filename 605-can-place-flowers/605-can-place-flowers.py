class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c = 0
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 0:
            return True
        
        if flowerbed[0] != 1 and flowerbed[1] != 1:
            flowerbed[0] = 1
            c += 1
        if flowerbed[-1] != 1 and flowerbed[-2] != 1:
            flowerbed[-1] = 1
            c += 1
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i-1] != 1 and flowerbed[i+1] != 1 and flowerbed[i] != 1:
                flowerbed[i] = 1
                c += 1
        
        return c >= n