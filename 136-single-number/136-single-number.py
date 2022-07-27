class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = []
        
        if len(nums) <= 1:
            return nums[0]
        
        for i in range(len(nums)):
            if nums[i] in s:
                s.remove(nums[i])
            else:
                s.append(nums[i])
                
        return s[0]