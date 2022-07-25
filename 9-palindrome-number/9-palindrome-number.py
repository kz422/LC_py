class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_char = str(x)
        reverse = x_char[::-1]
        if reverse == x_char:
            return reverse