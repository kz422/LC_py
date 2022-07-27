import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        # print(c.most_common()[0][0])
        return c.most_common()[0][0]