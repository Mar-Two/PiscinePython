#!/usr/bin/env python3
"""Bloc finally il permet de nettoyer"""


def water_plants(plant_list: list) -> None:
    """Simule le cycle d'arrosage avec nettoyage garanti."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise TypeError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except TypeError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Fonction de test de mes gestions d'erreur"""
    print("=== Garden Watering System ===\n")
    clean_list: list = ["tomate", "lettuce", "carrots"]
    wrong_list: list = ["tomate", None, "carrots"]
    print("Testing normal watering...")
    water_plants(clean_list)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    water_plants(wrong_list)
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
