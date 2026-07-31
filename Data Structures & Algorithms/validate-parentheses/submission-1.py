class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_dict = {'(': ')', '[': ']', '{': '}'}
        for i in range(len(s)):
            if s[i] in p_dict:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                elif s[i] == p_dict[stack.pop()]:
                    continue
                else:
                    return False
        return len(stack) == 0