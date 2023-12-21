# Widest Vertical Area Between Two Points Containing No Points 

# You are given n​​​​​​ points on a 2D plane.
# Each point has integer coordinates (xi, yi).
# Return the widest vertical area between two points such that no points are inside the area.
# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height).
# The widest vertical area is the one with the maximum width.
# Note that points on the edge of a vertical area are not considered included in the area.

# Example 1:
# Input: points = [[8,7],[9,9],[7,4],[9,7]]
# Output: 1

# Explanation: Both the red and the blue area are optimal.

# Example 2:
# Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# Output: 3

# Constraints:
# n == points.length
# 2 <= n <= 105
# points[i].length == 2
# 0 <= xi, yi <= 109

class Solution(object):
    def maxWidthOfVerticalArea(points):
        sorted_points = sorted(points, key=lambda x: x[0])
        max_width = 0
        for i in range(1, len(sorted_points)):
            width = sorted_points[i][0] - sorted_points[i-1][0]
            max_width = max(max_width, width)
        return max_width

    points = [[8,7],[9,9],[7,4],[9,7]]
    print(maxWidthOfVerticalArea(points))  # Output: 1

    points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
    print(maxWidthOfVerticalArea(points))  # Output: 3
