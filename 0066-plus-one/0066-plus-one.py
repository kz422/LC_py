class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        ls = ''.join((str(n) for n in digits))
        sum = int(ls) + 1
        
        return [int(x) for x in str(sum)]