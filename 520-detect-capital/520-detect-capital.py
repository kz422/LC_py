class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        u = word.upper()
        l = word.lower()
        d = word[1:]
        if u == word:
            return True
        elif l == word:
            return True
        elif word[0].isupper() and d.islower():
            return True
        return False