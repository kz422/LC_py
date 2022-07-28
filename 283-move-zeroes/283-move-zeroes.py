class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## model solution
        nums.sort(key=bool, reverse=True)
        
        ## my solution - solved but late
        if len(nums) == 1:
            nums = nums
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
                    
        print(nums)