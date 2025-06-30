COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors):
    result = int(color_code(colors[0])) * 10
    result += int(color_code(colors[1]))

    return result


def color_code(color):
    return COLORS.index(color)
