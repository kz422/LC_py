class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = [x.strip() for x in s.split()]
        return len(l[-1])