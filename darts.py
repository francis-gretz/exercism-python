OUTER_RADIUS = 10
MIDDLE_RADIUS = 5
INNER_RADIUS = 1


def is_in_circle(distance, radius):
    # x² + y² <= radius².
    # distance <= radius².
    return distance <= radius ** 2


def score(x, y):
    # distance = x² + y²
    distance = x ** 2 + y ** 2

    if (is_in_circle(distance, INNER_RADIUS)):
        return 10

    if (is_in_circle(distance, MIDDLE_RADIUS)):
        return 5

    if (is_in_circle(distance, OUTER_RADIUS)):
        return 1

    return 0
