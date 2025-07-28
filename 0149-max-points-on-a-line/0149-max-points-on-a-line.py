from math import sqrt, ceil

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return n

        lines = {}
        for i in range(n - 1):
            for j in range(i+1, n):
                lines[(i, j)] = 0

        for [x3, y3] in points:
            for [i, j] in lines:
                x1, y1 = points[i]
                x2, y2 = points[j]
                if (x3 - x1) * (y2 - y1) == (x2 - x1) * (y3 - y1):
                    lines[(i, j)] += 1

        max_points = 0
        for line in lines:
            max_points = max(max_points, lines[line])

        return max_points
