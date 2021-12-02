from vector import VECTOR_COMMAND_MAP


def command_to_vector2(command):
    """Given a text command, create a 2-dimensional vector with the appropriate
    direction and magnitude"""
    try:
        direction, magnitude = command.strip().split()
    except Exception:
        print("Failed to parse:", command)
    vector = VECTOR_COMMAND_MAP[direction]
    vector = vector.scale(int(magnitude))
    return vector

