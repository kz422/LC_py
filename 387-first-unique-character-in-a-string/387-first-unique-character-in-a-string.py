import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ## model solution
        count = collections.Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
    
        ## my solution - timed out
        l = list(s)
        # c = collections.Counter(l)
        for i in range(len(s)):
            if l.count(l[i]) == 1:
                return i

        return - 1