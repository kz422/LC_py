class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        
        li = [i for i, x in enumerate(nums) if x == target]
        
        return [li[0], li[-1]]