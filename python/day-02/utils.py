from vector import VECTOR_COMMAND_MAP, POSITION_AIM_COMMAND_MAP


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


def command_to_pos_aim_vectors(command):
    try:
        direction, magnitude = command.strip().split()
    except Exception:
        print("Failed to parse:", command)

    vec_pos, vec_aim = POSITION_AIM_COMMAND_MAP[direction]
    pos_delta = vec_pos.scale(int(magnitude))
    aim_delta = vec_aim.scale(int(magnitude))

    return pos_delta, aim_delta
