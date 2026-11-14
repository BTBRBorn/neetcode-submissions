# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        insertions = [pairs[:]]
        for i in range(1, len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j+1].key < pairs[j].key:
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                print("while loop.")
                j -= 1
            insertions.append(pairs[:])
        return insertions
        