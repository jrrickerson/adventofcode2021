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


def intersect_1d(p1, p2, p3, p4):
    """Find the intersection, if any, of two line segments on the same line"""
    e1, e2 = sorted((p1, p2))
    e3, e4 = sorted((p3, p4))

    if e2 >= e3 and e4 >= e1:
        # Segments overlap, so find the interval with the two middle points
        ordered = sorted((e1, e2, e3, e4))
        return range(ordered[1], ordered[2] + 1)
    return []



def overlapping(segment_a, segment_b):
    """Return a list of integer points within the overlapping line segment
    formed by colinear line segments, if any. May contain a single point
    Expects integer coordinates and vertical or horizontal lines.
    Adapted from: https://eli.thegreenplace.net/2008/08/15/intersection-of-1d-segments
    """
    v1, v2 = segment_a
    v3, v4 = segment_b

    if v1.x == v2.x == v3.x == v3.x:
        # Vertical colinear
        return [(v1.x, y) for y in intersect_1d(v1.y, v2.y, v3.y, v4.y)]
    elif v1.y == v2.y == v3.y == v4.y:
        # Horizontal colinear
        return [(x, v1.y) for x in intersect_1d(v1.x, v2.x, v3.x, v4.x)]
    else:
        # Not horizontal or vertical, so we will not get
        # a whole number for the overlap
        return []


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
        # Unhandled case
        print("Degenerate intersection")
        return None


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
        intersect = intersection_point(a1, a2, b1, b2)
        return [intersect] if intersect else []
    return []
