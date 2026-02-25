#!/usr/bin/env python3
"""Module complet de gestion des plantes du jardin"""


class GardenError(Exception):
    """Exception de base pour tous les problèmes du jardin."""
    pass


class PlantError(GardenError):
    """Exception levée pour les problèmes liés aux plantes."""
    pass


class WaterError(GardenError):
    """Exception levée pour les problèmes liés à l'arrosage."""
    pass


class SunlightError(GardenError):
    """Exception levée pour les problèmes liés au soleil"""
    pass


class GardenManager:

    def __init__(self, name: str) -> None:
        """Construit le jardin"""
        self.name = name
        self.garden = []

    def add_plant(self, plant: str) -> None:
        """Ajoute les plantes"""
        try:
            if not plant:
                raise PlantError("Plant name cannot be empty!")
            self.garden.append(plant)
            print(f"Added {plant} successfully")
        except PlantError as e:
            print(f"Error plant adding: {e}")

    def water_plants(self) -> None:
        """Arrose les plantes et gère le système avec un bloc finally."""
        print("Opening watering system")
        try:
            for plant in self.garden:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, name: str, water: int, sun: int) -> None:
        """Vérifie la santé et lève une erreur"""
        if water > 10:
            raise WaterError(f"Water level {water} is too high (max 10)")
        if sun < 2:
            raise SunlightError(f"Sunlight hours {sun} is too low (min 2)")
        print(f"{name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    """Test complet des plantes"""
    print("=== Garden Management System ===\n")
    gm = GardenManager("My Smart Garden")

    print("Adding plants to garden...")
    gm.add_plant("tomato")
    gm.add_plant("lettuce")
    gm.add_plant("")

    print("\nWatering plants...")
    gm.water_plants()

    print("\nChecking plant health...")
    try:
        gm.check_health("tomato", 5, 8)
    except GardenError as e:
        print(f"Error checking tomato: {e}")

    try:
        gm.check_health("lettuce", 15, 8)
    except GardenError as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...\n")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
