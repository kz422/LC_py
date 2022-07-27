class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

## model answear
        #check length of string and unique characters and return if they don't match
        if len(s) != len(t) or len(set(s)) != len(set(t)): return False
		
        mapping = {}
		
		#Loop through each character and create maps for each index character if already not there
        for i in range(len(s)):
            
            if s[i] not in mapping: mapping[s[i]] = t[i]
            
			#if current mapped character not equal to the same index of t string return false
            if mapping[s[i]] != t[i]: return False        
        #If all goes true, return True
        return True
    
## my solution -> fail of edge case
#         sl = {}
#         tl = {}
#         for i in range(len(s)):
#             sl[s[i]] = i
#             tl[t[i]] = i
        
#         if len(sl) != len(tl):
#             return False
        
#         for i  in range(len(sl)):
#             if sl[s[i]] != tl[t[i]]:
#                 return False
#             else:
#                 return True