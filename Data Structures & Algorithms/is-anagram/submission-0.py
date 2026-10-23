class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charMap = {}
        for i in range(len(s)):
            if s[i] not in charMap:
                charMap[s[i]] = [1, 0]
            else:
                charMap[s[i]][0] += 1

            if t[i] not in charMap:
                charMap[t[i]] = [0, 1]
            else:
                charMap[t[i]][1] += 1
        
        for val in charMap.values():
            if val[0] != val[1]:
                return False
        return True
        


