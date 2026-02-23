#!/usr/bin/env python3
"""Module d'heritage de class."""


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

    def get_base_info(self) -> str:
        """Retourne les infos communes au Plant."""
        cls_name: str = self.__class__.__name__
        return f"{self.name} ({cls_name}): {self.height}cm, {self.age} days"


class Flower(Plant):
    """Représente une fleur."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialise une nouvelle instance de fleur.
        """
        super().__init__(name, height, age)
        self.color: int = color

    def bloom(self) -> None:
        """Message qui dis que la plante pousse bien."""
        print(f"{self.name} is blooming beautifully!\n")

    def get_base_info(self):
        return f"{super().get_base_info()} {self.color} color"


class Tree(Plant):
    """Représente un arbre."""
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 trunk_diameter: int) -> None:
        """
        Initialise une nouvelle instance de arbre.
        """
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self, n: int) -> None:
        """Affiche en mettre carrés l'ombre"""
        print(f"{self.name} provides {n} square meters of shade\n")

    def get_base_info(self):
        return f"{super().get_base_info()} {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    """Représente un vegetaux."""
    def __init__(self,
                 name: str,
                 height: int,
                 age: int,
                 harvest_season: str,
                 nutritional_value: str) -> None:
        """
        Initialise une nouvelle instance de Vegetaux.
        """
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def display_nutritional_value(self) -> None:
        """Afficher la valeur nutritionelle du vegetaux."""
        print(f"{self.name} is rich in {self.nutritional_value}\n")

    def get_base_info(self):
        return f"{super().get_base_info()} {self.harvest_season} harvest"


def ft_plant_types() -> None:
    """Fonction de teste qui instancie 2 objet de chaque types."""
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    print(rose.get_base_info())
    rose.bloom()
    cactus = Flower("Cactus", 15, 120, "green")
    print(cactus.get_base_info())
    cactus.bloom()
    oak = Tree("Oak", 500, 1825, 50)
    print(oak.get_base_info())
    oak.produce_shade(90)
    palmier = Tree("Palmier", 600, 1400, 100)
    print(palmier.get_base_info())
    palmier.produce_shade(78)
    tomate = Vegetable("Tomate", 80, 90, "summer harvest", "Vitamine C")
    carrot = Vegetable("Carrot", 20, 70, "autumn harvest", "beta-carotene")
    print(tomate.get_base_info())
    tomate.display_nutritional_value()
    print(carrot.get_base_info())
    carrot.display_nutritional_value()


if __name__ == "__main__":
    ft_plant_types()
