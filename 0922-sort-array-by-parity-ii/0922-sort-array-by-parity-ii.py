class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        
        for num in nums:
            if(num % 2 == 0):
                even.append(num)
            else:
                odd.append(num)
                
        result = [None]*(len(even)+len(odd))
        result[::2] = even
        result[1::2] = odd
        
        return result