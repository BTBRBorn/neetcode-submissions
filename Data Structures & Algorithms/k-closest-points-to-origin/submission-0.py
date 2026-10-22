import heapq

class Solution:
    def distance(self, point):
        x, y = point[0], point[1]
        return (x**2 + y**2)**1/2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closets = heapq.nsmallest(k, points, key=self.distance) 
        return closets
        
        