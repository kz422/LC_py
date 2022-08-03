import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9: 'wxyz'}
        a = []
        d = list(digits)
        
        f = 0
        s = 0
        t = 0
        fo = 0
        
        if len(d) == 0:
            return a
        elif len(d) == 1:
            return list(mp[int(d[0])])
        
        if len(d) == 2:
            f = int(d[0])
            s = int(d[1])
            com = list(itertools.product(list(mp[f]), list(mp[s])))
        elif len(d) == 3:
            f = int(d[0])
            s = int(d[1])
            t = int(d[2])
            com = list(itertools.product(list(mp[f]), list(mp[s]), list(mp[t])))
        elif len(d) == 4:
            f = int(d[0])
            s = int(d[1])
            t = int(d[2])
            fo = int(d[3])
            com = list(itertools.product(list(mp[f]), list(mp[s]), list(mp[t]), list(mp[fo])))
            
        for l in com:
            s = ''.join(l)
            a.append(s)
            
        return a