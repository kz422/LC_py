import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## model solution
        # return (sorted(list(s)) == sorted(list(t)))
        
        ## model solution 2
        return collections.Counter(s) == collections.Counter(t)
    
        ## my solution - solved but late
#         if len(s) != len(t):
#             return False
#         l = list(t)
#         for i in range(len(s)):
#             if s[i] in l:
#                 l.remove(s[i])
            
#         return True if not l else False