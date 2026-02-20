"""Module d'heritage de class exception"""


class GardenError(Exception):
    """Exception de base pour tous les problèmes du jardin."""
    pass


class PlantError(GardenError):
    """Exception levée pour les problèmes liés aux plantes."""
    pass


class WaterError(GardenError):
    """Exception levée pour les problèmes liés à l'arrosage."""
    pass


def check_type_erreur(name: str) -> None:
    """Vérifie le type d'erreur et la capture via la classe parente."""
    try:
        if name == "plant":
            raise PlantError("The tomato plant is wilting!")
        elif name == "water":
            raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")


def test_custom_errors() -> None:
    """Lance les tests demandés dans l'exercice."""
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("Testing catching all garden errors...")
    check_type_erreur("plant")
    check_type_erreur("water")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
