class Solution:
    def averageValue(self, nums: List[int]) -> int:
        li = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] % 3 == 0:
                li.append(nums[i])
        
        if len(li) == 0:
            return 0
        else:
            return int(sum(li) / len(li))