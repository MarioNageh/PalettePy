def extract_rgb_from_color(c):
    index = 0
    r, g, b = 0, 0, 0
    if type(c) is str:
        if len(c) < 0:
            raise Exception("Color Code Not Correct")
        if len(c) == 9 and c[0] != "#":
            raise Exception("Color Code Not Correct")
        if len(c) == 8 and c[0] == "#":
            raise Exception("Color Code Not Correct")

        if "0x" in c:
            raise Exception("Color Code Not Correct")

        if c[0] == "#":
            index = 1

        r = int(c[index:index + 2], 16)
        index += 2
        g = int(c[index:index + 2], 16)
        index += 2
        b = int(c[index:index + 2], 16)
        index += 2

    elif type(c) is int:
        b = get_n_bytes_from_int(c, 0)
        g = get_n_bytes_from_int(c, 1)
        r = get_n_bytes_from_int(c, 2)

    return r, g, b


def get_n_bytes_from_int(c, pos):
    shifted = c >> (8 * pos)
    masked = shifted & 0xff
    return masked

