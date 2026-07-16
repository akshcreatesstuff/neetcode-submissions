class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqMapA = {}
        freqMapB = {}
    
        for i in range(len(s)):
            freqMapA[s[i]] = freqMapA.get(s[i], 0) + 1
            freqMapB[t[i]] = freqMapB.get(t[i], 0) + 1

        return freqMapA == freqMapB

        