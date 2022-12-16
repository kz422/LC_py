class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        r = []
        l = []
        p = []
        for i in range(len(nums)):
            if nums[i] > pivot:
                r.append(nums[i])
            elif nums[i] < pivot:
                l.append(nums[i])
            else:
                p.append(nums[i])
        return (l+p+r)