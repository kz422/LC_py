class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(cnt%2==0 for c,cnt in Counter(nums).items())