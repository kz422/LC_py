import collections

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp = {}
        l = list(s.split(" "))
        if (len(set(pattern)) != len(set(l))) or len(pattern) != len(l):
            return False
        else: 
            for i in range(len(pattern)):
                if pattern[i] not in mp:
                    mp[pattern[i]] = l[i]
                elif mp[pattern[i]] != l[i]:
                    return False
            return True