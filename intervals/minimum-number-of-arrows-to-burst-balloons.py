# 452. Minimum Number of Arrows to Burst Balloons
# Time: O(n log n) | Space: O(1)
# Sort by end point, greedily place arrow at end of first balloon.
# New arrow needed only when next balloon starts after current arrow position.

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 0:
            return 0

        result = 1
        points.sort(key=lambda x: x[1])
        end = points[0][1]

        for i in range(1, len(points)):
            if end < points[i][0]:
                result += 1
                end = points[i][1]

        return result