import sys
import math


def main() -> None:
    """Calcule la distance entre deux point.
    Gere les erreurs de parsing et transforme l'argument en tuple.
    """
    print("=== Game Coordinate System ===\n")
    pos_dep: tuple = (0, 0, 0)
    pos_arr: tuple = (10, 20, 5)
    print(f"Position created: {pos_arr}")
    res: float = math.sqrt((pos_arr[0] - pos_dep[0])**2 +
                           (pos_arr[1] - pos_dep[1])**2 +
                           (pos_arr[2] - pos_dep[2])**2)
    print(f"Distance between {pos_dep} and {pos_arr}: {res:.2f}\n")
    try:
        value: str = sys.argv[1]
        newlist: list = [int(x) for x in value.split(',')]
        print(f"Parsing coordinates: \"{value}\"")
        av: tuple = tuple(newlist)
        print(f"Parsed position: {av}")
        res_av: float = math.sqrt((av[0] - pos_dep[0])**2 +
                                  (av[1] - pos_dep[1])**2 +
                                  (av[2] - pos_dep[2])**2)
        print(f"Distance between {pos_dep} and {av}: {res_av:.1f}\n")
        print("Unpacking demonstration:")
        x, y, z = av
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{sys.argv[1]}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: (\"{e}\",)")


if __name__ == "__main__":
    main()
