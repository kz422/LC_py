import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = list(itertools.permutations(nums))
        ans = []
        for i in range(len(l)):
            ans.append(list(l[i]))
            
        return ans