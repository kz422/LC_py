class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        srt = sorted(score, reverse=True)
        ans = []
        for i in range(len(score)):
            if score[i] == srt[0]:
                ans.append("Gold Medal") 
            elif score[i] == srt[1]:
                ans.append('Silver Medal')
            elif score[i] == srt[2]:
                ans.append("Bronze Medal")
            else:
                ans.append(str(srt.index(score[i])+1))
        return ans
            