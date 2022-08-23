class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        for i in range(len(s)):
            if s[i].isalnum():
                a.append(s[i].lower())
        # print(''.join(a)[::-1])
        return ''.join(a) == ''.join(a)[::-1]
        