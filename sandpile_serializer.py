import sys
import json
import sandpile_generator


def serialize_sandpile(no_of_sand_grains, max_grains_per_field):
    """
    Creates a JSON file for a generated sandpile fractal with the given parameters
    :param no_of_sand_grains:  Number of grains to distribute
    :param max_grains_per_field:  Maximum number of grains allowed on a field
    :return: The generated JSON string
    """
    sandpile = sandpile_generator.generate_sandpile_matrix(
            no_of_sand_grains, max_grains_per_field)
    return json.dumps({str(k): v for k, v in sandpile.items()})


if __name__ == '__main__':
    assert len(sys.argv) >= 3
    print(serialize_sandpile(int(sys.argv[1]), int(sys.argv[2])))