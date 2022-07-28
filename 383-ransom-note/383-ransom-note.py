class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l = list(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] not in l:
                return False
            else:
                l.remove(ransomNote[i])
                
        return True