class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        n = len(s)
        half = n//2
        if n % 2 == 0:
            p = str(s[0:half]) + str(s[0:half][::-1])
        else:
            p = str(s[0:half]) + s[half] + str(s[0:half][::-1])
        
        return s == p

        