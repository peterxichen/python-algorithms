# Valid Parentheses
# single pass w/ stack, pop if ), else append
# time O(n), space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == ')':
                if '(' != (stack.pop() if stack else None):
                    return False
            elif c == '}':
                if '{' != (stack.pop() if stack else None):
                    return False
            elif c == ']':
                if '[' != (stack.pop() if stack else None):
                    return False
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        else:
            return False
