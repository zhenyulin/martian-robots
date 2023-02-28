ORIENTATIONS = "NESW"


def parse_coordinates(coordinates_or_positions):
    """parse both surface coordinates and robot positions

    Args:
            coordinates_or_positions (String)

    Returns:
            tuple(Int, Int, Any): with coordinates parsed as Int
    """
    chars = coordinates_or_positions.split(" ")
    return (int(chars[0]), int(chars[1]), *chars[2:])


def parse_input(text):
    """parse the string input into Tuple and List

    The first line of input is the max coordinates of the 2D surface

    The remaining input consists of a sequence of robot positions and instructions (two lines per robot). A position consists of two integers specifying the initial coordinates of the robot and an orientation (N, S, E, W), all separated by whitespace on one line. A robot instruction is a string of the letters “L”, “R”, and “F” on one line.

    Args:
        text (String): input to define the surface and for each robot
    """
    lines = [line for line in map(lambda x: x.strip(), text.splitlines()) if len(line)]

    surface = parse_coordinates(lines[0])
    robots = [
        (parse_coordinates(lines[i]), lines[i + 1]) for i in range(1, len(lines), 2)
    ]

    return surface, robots


def move(surface, positions, instructions, hints=set()):
    """return the position of the robot on the given surface after instructions

    Given a 2D surface with the range defined by coordinates surface,
    the robot start at positions and followed instructions,
    return the final positions of the robots

    * there can be further types of instructions

    Args:
        surface (Tuple): the max coordinates of the surface, e.g. '5 3' (max 50)
        positions (String): the starting coordinates and orientation of the robot, e.g. '1 1 E'
        instructions (String): the instruction sequence for the robot, e.g. 'RFFLF' (less than 100 chars)
        hints (Set): the set of coordinates that previous robots went LOST
    """
    a, b = surface
    x, y, o = positions

    for i in instructions:
        if i == "L":
            o = ORIENTATIONS[ORIENTATIONS.index(o) - 1]
        elif i == "R":
            o = ORIENTATIONS[(ORIENTATIONS.index(o) + 1) % 4]
        elif i == "F":
            _x, _y = x, y
            if o == "E":
                x += 1
            elif o == "W":
                x -= 1
            elif o == "N":
                y += 1
            elif o == "S":
                y -= 1

            if not (0 <= x <= a and 0 <= y <= b):
                if (_x, _y) in hints:
                    x, y = _x, _y
                else:
                    return True, _x, _y, o
        else:
            raise Exception(f"invalid command found - {i}")

    return False, x, y, o


def main(input_text):
    """Given a surface and list of robots, return the final positions of each robot

    The robots know where previous robots fell off the surface and can avoid that based records.

    The first line of input is the max coordinates of the 2D surface

    The remaining input consists of a sequence of robot positions and instructions (two lines per robot). A position consists of two integers specifying the initial coordinates of the robot and an orientation (N, S, E, W), all separated by whitespace on one line. A robot instruction is a string of the letters “L”, “R”, and “F” on one line.

    Args:
      text (String): input to define the surface and for each robot

    Returns:
      [String]: the final positions of each robot
    """
    surface, robots = parse_input(input_text)

    hints, output = set(), ""

    for (positions, instructions) in robots:
        falloff, x, y, o = move(surface, positions, instructions, hints)

        output += f"{x} {y} {o}"

        if falloff:
            hints.add((x, y))
            output += " LOST"

        output += "\n"

    return output
