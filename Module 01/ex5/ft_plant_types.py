"""Module d'heritage de class"""


class Plant:
    """
    Represente une plante avec son nom, taille et age.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """
        Initialise une nouvelle instance de Plant
        """
        self.name = name
        self.height = height
        self.age = age

    def get_base_info(self) -> str:
        """Retourne les infos communes au Plant."""
        cls_name: str = self.__class__.__name__
        return f"{self.name} ({cls_name}): {self.height}cm, {self.age} days"


class Flower(Plant):
    """Représente une fleur"""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """
        Initialise une nouvelle instance de fleur.
        """
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Message qui dis que la plante pousse bien."""
        print(f"{self.name} is blooming beautifully!")


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
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Affiche en mettre carrés l'ombre"""
        print(f"{self.name} provides 78 square meters of shade")


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
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def display_nutritional_value(self) -> None:
        """Afficher la valeur nutritionelle du vegetaux."""
        print(f"{self.name} is rich in {self.nutritional_value}")


def ft_plant_types() -> None:
    """Fonction de teste qui instancie 2 objet de chaque types."""
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    print(f"{rose.get_base_info()}, {rose.color} color")
    rose.bloom()
    cactus = Flower("Cactus", 15, 120, "green")
    print(f"{cactus.get_base_info()}, {cactus.color} color")
    cactus.bloom()
    oak = Tree("Oak", 500, 1825, 50)
    print(f"{oak.get_base_info()}, {oak.trunk_diameter}cm diameter")
    oak.produce_shade()
    palmier = Tree("Palmier", 600, 1400, 100)
    print(f"{palmier.get_base_info()}, {palmier.trunk_diameter}cm diameter")
    palmier.produce_shade()
    tomate = Vegetable("Tomate", 80, 90, "summer harvest", "Vitamine C")
    carrot = Vegetable("Carrot", 20, 70, "autumn", "beta-carotene")
    print(f"{tomate.get_base_info()}, {tomate.harvest_season}")
    tomate.display_nutritional_value()
    print(f"{carrot.get_base_info()}, {carrot.harvest_season}")
    carrot.display_nutritional_value()


if __name__ == "__main__":
    ft_plant_types()
