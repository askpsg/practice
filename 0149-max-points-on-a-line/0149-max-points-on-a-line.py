from math import sqrt, floor, gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 3:
            return n

        lines = {}
        for i in range(n - 1):
            [x1, y1] = points[i]
            for j in range(i + 1, n):
                if i == j:
                    continue

                [x2, y2] = points[j]
                x = x2 - x1
                y = y2 - y1
                g = gcd(x, y)
                x, y = x//g, y//g
                m = y/x if x else 'inf'
                c = (y1*x - x1*y)/x if x else x1
                lines[(m, c)] = lines.get((m, c), 0) + 1

        return ceil(sqrt(2*max(lines.values())))
