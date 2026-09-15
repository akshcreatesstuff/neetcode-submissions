class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(s) - 1
        for i in range(len(s)//2):
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        