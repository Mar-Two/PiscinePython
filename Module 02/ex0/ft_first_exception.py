
def check_temperature(temp_str: str) -> int | None:
    """
    Valide si une chaîne de caractères représente une température
    acceptable pour les plantes (0-40°C).
    """
    try:
        n: int = int(temp_str)
        if n < 0:
            print(f"Error: {n}°C is too cold for plants (min 0°C)")
            return None
        if n > 40:
            print(f"Error: {n}°C is too hot for plants (max 40°C)")
            return None
        print(f"Temperature {n}°C is perfect for plants!")
        return n

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input() -> None:
    """Function qui check plusieurs valeurs."""
    print("=== Garden Temperature Checker ===")
    temp_test: list = ["25", "abc", "100", "-50"]
    for temp in temp_test:
        print(f"Testing temperature: {temp}")
        check_temperature(temp)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
