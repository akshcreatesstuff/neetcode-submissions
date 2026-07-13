class Solution:
    def isValid(self, s: str) -> bool:
        char_stack = []

        char_map = {
            ')' :'(',
            '}' : '{',
            ']' : '[' 
        }

        for ch in s:
            if ch in char_map:
                if char_stack and char_stack[-1] == char_map[ch]:
                    char_stack.pop()
                else:
                    return False
            else:
                char_stack.append(ch)
        return len(char_stack) == 0
        