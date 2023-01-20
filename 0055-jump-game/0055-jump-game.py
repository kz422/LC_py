class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i-1] < i: return False 
            nums[i] = max(nums[i-1], i+nums[i])
        return True