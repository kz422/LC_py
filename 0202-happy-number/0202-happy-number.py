class Solution:
    def isHappy(self, n: int) -> bool:
        while(n > 9) : n = sum(int(c)**2 for c in str(n))
        return True if n in (1, 7) else False