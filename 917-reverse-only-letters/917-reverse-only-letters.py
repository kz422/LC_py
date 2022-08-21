class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        r = [s for s in S if s.isalpha()]
        return "".join(S[i] if not S[i].isalpha() else r.pop() for i in range(len(S)))
#         a = []
#         al = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#         for i in range(len(s)):
#             if s[-(i+1)] not in al:
#                 a.append(s[-(i+1)])
            
#         return "".join(a)