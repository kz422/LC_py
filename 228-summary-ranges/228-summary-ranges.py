class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ## model solution
        ret=[]
        save=""
        for i in range(len(nums)):
            if i<=len(nums)-2 and nums[i+1] == nums[i]+1:
                if save == "":
                    save=str(nums[i]) + "->"
            else:
                ret.append(save+str(nums[i]))
                save=""

        return ret
    
        ## my solution (not completed)
#         l = []
#         for i in range(len(nums) - 1):
#             if nums[i] - nums[i +1] <= 1:
#                 l.append(str(nums[i]))
#             else:
#                 l.append(nums[i])
                
#         print(l)