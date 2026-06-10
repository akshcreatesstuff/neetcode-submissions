class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqA = {} 
        freqB = {}
        for i in range(len(s)):
            freqA[s[i]] = freqA.get(s[i], 0) + 1
            freqB[t[i]] = freqB.get(t[i], 0) + 1
            
        return freqA == freqB