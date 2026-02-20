"""Module de simulation de pousse."""


class Plant:
    """Représente une plante avec son nom, taille et âge."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialise une nouvelle instance de Plant."""
        self.name = name
        self.height = height
        self.current_age = age

    def grow(self, cm: int) -> None:
        """Augmente la taille de la plante de 'cm' centimètres."""
        self.height += cm

    def age(self) -> None:
        """Vieillit la plante d'un jour."""
        self.current_age += 1

    def get_info(self) -> str:
        """Retourne une chaîne décrivant l'état de la plante."""
        return f"{self.name}: {self.height}cm, {self.current_age} days old"


def ft_plant_growth() -> None:
    """Simulateur de pousse de plante qui affiche ça progression."""

    plant = Plant("Rose", 25, 30)
    first_height: int = plant.height
    print("=== Day 1 ===")
    print(plant.get_info())
    for n in range(6):
        plant.grow(1)
        plant.age()
    last_height: int = plant.height
    result: int = last_height - first_height
    print("=== Day 7 ===")
    print(plant.get_info())
    print(f"Growth this week: +{result}cm")


if __name__ == "__main__":
    ft_plant_growth()
