import collections
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
#         nums.sort()
#         ans = []
#         for i in range(len(nums)):
#             if i+1 != nums[i]:
#                 ans.append(nums[i])
#                 ans.append(i+1)
                
#         return ans
    
        n = len(nums)
        s = n*(n+1)//2
        miss = s - sum(set(nums))
        duplicate = sum(nums) + miss - s
        return [duplicate, miss]