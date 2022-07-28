class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l = list(t)
        for i in range(len(s)):
            if s[i] in l:
                l.remove(s[i])
            
        return True if not l else False