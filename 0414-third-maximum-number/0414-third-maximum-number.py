class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        setNums = set(nums)
        if len(setNums) <= 2:
            return max(setNums)
        return sorted(setNums)[-3]