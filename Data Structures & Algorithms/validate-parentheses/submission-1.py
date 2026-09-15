class Solution:
    def isValid(self, s: str) -> bool:
        symbols = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        compute_stack = []

        for ch in s:
            if ch in symbols:
                if compute_stack and compute_stack[-1] == symbols[ch]:
                    compute_stack.pop()
                else:
                    return False
            else:
                compute_stack.append(ch)
        return len(compute_stack) == 0