class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        n = len(s)
        if n == 0: return True
        if n % 2 == 0:
            half = n // 2
            p = str(s[0:half] + s[0:half][::-1])
        else:
            half = n // 2
            p = str(s[0:half] + s[half] + s[0:half][::-1])
        return p == s