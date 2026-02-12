"""Module qui crée et affiche differentes plantes."""


class Plant:
    """Représente une plante avec son nom, taille et âge."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialise une nouvelle instance de Plant."""
        self.name = name
        self.height = height
        self.current_age = age

    def get_info(self) -> str:
        """Return les infos actuel de l'objet."""
        return f"{self.name} ({self.height}cm, {self.current_age} days)"


def ft_plant_factory() -> None:
    """Crée 5 plante et affiche leurs infos."""
    garden: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
        Plant("Oak", 200, 365),
        Plant("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    for i in range(5):
        plante = garden[i]
        print("Created:", plante.get_info())
    print("Total plants created: 5")


if __name__ == "__main__":
    ft_plant_factory()
