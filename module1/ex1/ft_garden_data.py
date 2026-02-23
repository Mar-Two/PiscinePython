#!/usr/bin/env python3

"""
Module d'Instance d'objet plant.
"""


class Plant:
    """
    Represente une plante avec son nom, taille et age.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialise une nouvelle instance de Plant.
        """
        self.name: str = name
        self.height: int = height
        self.age: int = age


def ft_garden_data() -> None:
    """
    Crée plusieurs instances de plantes et les affiche.
    """

    garden: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    print("=== Garden Plant Registry ===")
    for i in range(3):
        plant = garden[i]
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    ft_garden_data()
