class Solution:
    def calcDist(self, pair):
        return pair[0] ** 2 + pair[1] ** 2
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        solution = []
        dists = list(map(self.calcDist, points))
        sort_dists = sorted(dists)
        for i in range(k):
            index = dists.index(sort_dists[i])
            solution.append(points[index])
            dists[index] = None
        
        return solution
