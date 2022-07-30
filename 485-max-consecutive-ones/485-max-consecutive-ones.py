class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        ct = 0
        for num in nums:
            if num == 1:
                ct += 1
                ans = max(ans, ct)
            else:
                ct = 0
        return ans