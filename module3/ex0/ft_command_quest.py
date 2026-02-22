import sys


def main() -> None:
    """Compte le nombre d'arguments."""
    n: int = len(sys.argv)
    print("=== Command Quest ===")
    if n <= 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {n}")
    else:
        i: int = 1
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {n - 1}")
        while i < n:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print(f"Total arguments: {n}")


if __name__ == "__main__":
    main()
