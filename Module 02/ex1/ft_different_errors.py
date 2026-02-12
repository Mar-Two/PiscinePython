

def garden_operations() -> None:
    """Teste différents types d'erreurs."""
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        14 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    print("Testing KeyError...")
    try:
        garden: dict[str, int] = {"roses": 5}
        _ = garden["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    print("Testing multiple errors together...")
    try:
        int("abc")
        14 / 0
        open("missing.txt")
        garden = {"roses": 5}
        print(garden["missing_plant"])
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    """Lance la démonstration des erreurs."""
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
