class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            nums = nums
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
        # for i in range(len(nums)):
        #     for j in range(len(nums) - 1 - i):
        #         if nums[j] == 0:
        #             nums.remove(nums[j])
        #             nums.append(0)
        #         if nums[j] > nums[j + 1]:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    
        print(nums)