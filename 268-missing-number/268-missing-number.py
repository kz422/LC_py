class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ## model solution
        n = len(nums)
        return n * (n+1) // 2 - sum(nums)
    
        ## my solution - solved but late
        for i in range(len(nums) + 1):
            if i not in nums:
                return i