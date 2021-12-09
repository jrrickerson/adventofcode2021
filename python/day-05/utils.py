import math
from vector import Vector2


def parse_vector_pairs(line):
    if not line:
        return None, None

    coords1, coords2 = line.strip().split("->")
    x1, y1 = coords1.strip().split(",")
    x2, y2 = coords2.strip().split(",")

    v1 = Vector2(int(x1), int(y1))
    v2 = Vector2(int(x2), int(y2))

    return v1, v2


def is_horizontal_segment(vector_start, vector_end):
    return vector_start.y == vector_end.y


def is_vertical_segment(vector_start, vector_end):
    return vector_start.x == vector_end.x


def is_diagonal_segment(vector_start, vector_end):
    """Diagonal as defined by a slope of 1 or -1"""
    return slope(vector_start, vector_end) in (1, -1)


def is_nonzero_segment(vector_start, vector_end):
    """Return True if the segment has a nonzero length"""
    return not (
        vector_start.x == vector_end.x and
        vector_start.y == vector_end.y)


def sign(val):
    """Returns 0 for 0, 1 for positive numbers, and -1 for negative numbers"""
    if val:
        return -1 if val < 0 else 1
    return 0


def slope(v1, v2):
    den = (v1.x - v2.x)
    return (v1.y - v2.y) / den if den else math.inf


def intersect_1d(p1, p2, p3, p4):
    """Find the intersection, if any, of two line segments on the same line"""
    e1, e2 = sorted((p1, p2))
    e3, e4 = sorted((p3, p4))

    if e2 >= e3 and e4 >= e1:
        # Segments overlap, so find the interval with the two middle points
        ordered = sorted((e1, e2, e3, e4))
        return range(ordered[1], ordered[2] + 1)
    return []


def line_coeff_from_endpoints(p1, p2):
    """Given two points on a line, find the coefficients of the line
    equation ax + by + c = 0"""
    a = p1.y - p2.y
    b = p2.x - p1.x
    c = -a * p1.x - b * p1.y
    return a, b, c


def determinent(a, b, c, d):
    return a * d - b * c


def intersect_2d(v1, v2, v3, v4):
    """Given 4 vectors representing start and end points of two
    line segments, find the intersection point, if it exists"""
    m = line_coeff_from_endpoints(v1, v2)
    n = line_coeff_from_endpoints(v3, v4)

    zn = determinent(m[0], m[1], n[0], n[1])

    x = -determinent(m[2], m[1], n[2], n[1]) / zn
    y = -determinent(m[0], m[2], n[0], n[2]) / zn

    return (x, y)


def overlapping(segment_a, segment_b):
    """Return a list of integer points within the overlapping line segment
    formed by colinear line segments, if any. May contain a single point
    Expects integer coordinates and vertical or horizontal lines.
    Adapted from: https://eli.thegreenplace.net/2008/08/15/intersection-of-1d-segments
    """
    v1, v2 = segment_a
    v3, v4 = segment_b

    if v1.x == v2.x == v3.x == v3.x:
        # Vertical colinear - find y delta of midpoints
        return [(v1.x, y) for y in intersect_1d(v1.y, v2.y, v3.y, v4.y)]
    elif v1.y == v2.y == v3.y == v4.y:
        # Horizontal colinear - find x delta of midpoints
        return [(x, v1.y) for x in intersect_1d(v1.x, v2.x, v3.x, v4.x)]
    else:
        # Diagonal colinear - generate points between the max of left
        # vector and the min of the right vector endpoints
        if v2 < v1:
            v1, v2 = v2, v1
        if v4 < v3:
            v3, v4 = v4, v3
        left = max(v1, v3)
        right = min(v2, v4)
        dx = sign(right.x - left.x)
        dy = sign(right.y - left.y)
        print("Diagonal interval:", left, right, dx, dy)
        x, y = left.x, left.y
        points = [(x, y)]
        while (x, y) != (right.x, right.y):
            x += dx
            y += dy
            points.append((x, y))
        return points


def intersection_point(v1, v2, v3, v4):
    """Assuming horizontal and vertical lines, find the intersection
    point between the line segment v1->v2 and v3->v4"""
    if v1.x == v2.x and v3.y == v4.y:
        # First segment is horizontal, second is vertical
        return (v1.x, v3.y)
    elif v1.y == v2.y and v3.x == v4.x:
        # First segment is vertical, second is horizontal
        return (v3.x, v1.y)
    else:
        slope1 = slope(v1, v2)
        slope2 = slope(v3, v4)
        if (slope1 not in (-1, 0, 1, math.inf) or
                slope2 not in (-1, 0, 1, math.inf)):
            print("Slope of line segment outside expectations!")
        # Ugly brute force for diagonals for now
        dx1 = sign(v2.x - v1.x)
        dy1 = sign(v2.y - v1.y)
        delta1 = max(abs(v1.x - v2.x), abs(v1.y - v2.y))
        points1 = [
            (v1.x + dx1 * i, v1.y + dy1 * i)
            for i in range(delta1 + 1)]
        #print(f"dx={dx1}, dy={dy1}, Points1", points1)
        dx2 = sign(v4.x - v3.x)
        dy2 = sign(v4.y - v3.y)
        delta2 = max(abs(v3.x - v4.x), abs(v3.y - v4.y))
        points2 = [
            (v3.x + dx2 * i, v3.y + dy2 * i)
            for i in range(delta2 + 1)]
        #print(f"dx={dx2}, dy={dy2}, Points2", points2)
        intersecting = set(points1) & set(points2)
        return intersecting.pop() if intersecting else None


def intersections(segment_a, segment_b):
    """Determine if two line segments, specified by their endpoint
    vectors, have intersecting points, and return the count of intersecting
    points.
    - Returns 0 for non-intersecting segments
    - Returns 1 for perpendicular segments
    - Returns > 1 for overlapping segments on the same line

    Algorithms blatently stolen and adapted from:
        https://stackoverflow.com/a/565282
        https://cp-algorithms.com/geometry/check-segments-intersection.html
    """
    # Split segments into start and end vectors
    a1, a2 = segment_a
    b1, b2 = segment_b

    if b1.cross_to(a1, b2) == 0 and b1.cross_to(a2, b2) == 0:
        # No intersection, but they might be colinear
        return overlapping(segment_a, segment_b)
    if (sign(a1.cross_to(a2, b1)) != sign(a1.cross_to(a2, b2)) and
            sign(b1.cross_to(b2, a1)) != sign(b1.cross_to(b2, a2))):
        point = intersect_2d(a1, a2, b1, b2)
        return [(int(point[0]), int(point[1]))] if point else []
    return []
