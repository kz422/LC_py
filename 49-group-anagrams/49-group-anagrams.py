import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in h:
                h[sortedWord] = [word]
            else:
                h[sortedWord].append(word)
        final = []
        for value in h.values():
            final.append(value)
        return final
#         mp = {}
#         for i in range(len(strs)):
#             li = "".join(sorted(list(strs[i])))
#             mp[li] = strs[i]
            
#         print(mp)