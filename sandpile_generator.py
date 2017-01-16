import collections


def generate_sandpile_matrix(no_of_sand_grains, max_grains_per_field):
    """
    Generates are matrix with the number of sand grains.
    :param no_of_sand_grains:  Number of grains to distribute
    :param max_grains_per_field:  Maximum number of grains allowed on a field
    :return: Dictionary in the form of (x, y) -> no of sand grains
    """
    matrix = collections.defaultdict(lambda : 0)
    matrix[(0,0)] = no_of_sand_grains

    matrix_changed = True
    while matrix_changed:
        matrix_changed = False
        m2 = matrix.copy()
        for position, sand in m2.items():
            if sand > max_grains_per_field:
                x, y = position
                matrix[position] -= 4
                matrix[(x + 1, y)] += 1
                matrix[(x - 1, y)] += 1
                matrix[(x, y + 1)] += 1
                matrix[(x, y - 1)] += 1
                matrix_changed = True
    return matrix
