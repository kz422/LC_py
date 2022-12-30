class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        
        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)

        result = [None]*(len(pos)+len(neg))
        result[::2] = pos
        result[1::2] = neg
    
        return result