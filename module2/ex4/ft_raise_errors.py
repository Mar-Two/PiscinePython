#!/usr/bin/env python3
"""Module de gestion d'erreur"""


def check_plant_health(
        plant_name: str, water_level: int, sunlight_hours: int
        ) -> str:
    """Valide les paramètres de santé d'une plante."""
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Exécute la suite de tests de validation."""
    print("=== Garden Plant Health Checker ===")
    print("Testing good values...")
    try:
        result: str = check_plant_health("tomate", 6, 7)
        print(f"{result}\n")
    except ValueError as e:
        print(f"Error: {e}\n")
    print("Testing empty plant name...")
    try:
        check_plant_health("", 6, 7)
    except ValueError as e:
        print(f"Error: {e}\n")
    print("Testing bad water level...")
    try:
        check_plant_health("carrot", 15, 7)
    except ValueError as e:
        print(f"Error: {e}\n")
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("carrot", 6, 0)
    except ValueError as e:
        print(f"Error: {e}\n")
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
