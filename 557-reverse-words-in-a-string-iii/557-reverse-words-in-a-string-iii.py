class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(' ')
        ans = []
        
        for i in range(len(l)):
            ans.append(l[i][::-1])
        
        return ' '.join(ans)