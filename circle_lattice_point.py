def lattice_point(x, y, r):
    coord = []
    temp = [i for i in range(r + 1)] + [i for i in range(r - 1, -1, -1)]
    for i, k in enumerate(range(y + r, y - r - 1, -1)):
        for j in range(x + temp[i], x - temp[i] - 1, -1):
            coord.append((j, k))

    return coord


def solution(circles: list):
    """circles: list[(x, y, r),]"""

    position = set()
    for circle in circles:
        for coord in lattice_point(*circle):
            position.add(coord)

    return len(position)


print(solution([(3, 3, 2), (2, 2, 1)]))
