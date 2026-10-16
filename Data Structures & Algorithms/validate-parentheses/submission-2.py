class Solution:
    def isValid(self, s: str) -> bool:
        bag = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        check_stack = []

        for c in s:
            if c in bag:
                if check_stack and check_stack[-1] == bag[c]:
                    check_stack.pop()
                else:
                    return False
            else:
                check_stack.append(c)
        return len(check_stack) == 0