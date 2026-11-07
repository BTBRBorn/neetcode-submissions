class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def longest(p1: int, p2: int) ->  int:
            if p1 == len(text1) or p2 == len(text2):
                return 0

            if (p1, p2) in cache:
                return cache[(p1, p2)]

            if text1[p1] == text2[p2]:
                count = 1 + longest(p1 + 1, p2 + 1) 
            else:
                count = max(longest(p1 + 1, p2), longest(p1, p2 + 1))

            cache[(p1, p2)] = count

            return count
        
        return longest(0, 0)


            

        