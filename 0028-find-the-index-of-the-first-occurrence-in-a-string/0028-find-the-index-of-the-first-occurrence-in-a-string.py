class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        
        return haystack.find(needle)
        
        # return -1 if needle not in haystack else haystack.find(needle)