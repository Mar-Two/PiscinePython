"""Module d'heritage multiple et d'organisation de méthodes."""


class Plant:
    """Initialise une plante."""
    def __init__(self, name: str, height: int) -> None:
        """Construit l'objet."""
        self.name = name
        self.height = height
        self.kind = "regular"

    def get_description(self) -> None:
        """Retourne la desription basic."""
        return f"{self.name}: {self.height}cm"

    def get_score_contribution(self) -> int:
        """Retourne la taille"""
        return self.height


class FloweringPlant(Plant):
    """Initialise une plante avec une couleur."""
    def __init__(self,
                 name: str,
                 height: int,
                 color: str,
                 ) -> None:
        """Construit l'objet."""
        super().__init__(name, height)
        self.color = color
        self.kind = "flowering"

    def get_description(self) -> str:
        base = super().get_description()
        """Retourne la desription basic + la couleur."""
        return f"{base}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """Initialise une plante avec un bonus de point."""
    def __init__(self,
                 name: str,
                 height: int,
                 color: str,
                 point: int) -> None:
        super().__init__(name, height, color)
        """Construit l'objet."""
        self.point = point
        self.kind = "prize flower"

    def get_description(self) -> str:
        """Retourne la desription basic + le bonus de point."""
        base = super().get_description()
        return f"{base}, Prize points: {self.point}"

    def get_score_contribution(self) -> int:
        """Retourne la taille + le bonus * 4."""
        return self.height + (self.point * 4)


class GardenManager:
    """Class qui manage et analyse un jardin."""
    total_jardin = 0

    def __init__(self, name) -> None:
        """Construit le jardin et compte le nombre de jardins."""
        self.name = name
        self.garden = []
        self.total_gr = 0
        self.total_plant = 0
        GardenManager.total_jardin += 1

    def add_plant(self, plant: any) -> None:
        """Ajoute les plantes et les comptes."""
        self.garden.append(plant)
        print(f"Added {plant.name} to {self.name}")
        self.total_plant += 1

    def growth(self) -> None:
        """Faire pousser les plantes."""
        print(f"{self.name} is helping all plants grow...")
        for plant in self.garden:
            plant.height += 1
            self.total_gr += 1
            print(f"{plant.name} grew 1cm")
        print("\n")

    @classmethod
    def create_garden_network(cls) -> None:
        """Initialise le réseau global pour tous les jardins créés."""
        print(f"Total gardens managed: {cls.total_jardin}")

    class GardenStats:
        @staticmethod
        def calcul_stat(plants_list: list) -> int:
            """Méthode statique utilitaire qui calcule le score."""
            total: int = 0
            for plant in plants_list:
                total += plant.get_score_contribution()
            return total

    @staticmethod
    def validate_height(plants: list) -> bool:
        """Méthode statique utilitaire
        qui renvoie un booleen si toutes les tailles sont positives.
        """
        for pl in plants:
            if pl.height <= 0:
                return False
        return True

    def affiche_stat_garden(self) -> None:
        """Methode qui affiche les stats du jardin."""
        print("=== Alice's Garden Report ===")
        print("Plants in garden:")
        for plant in self.garden:
            print(f"- {plant.get_description()}")
        print("\n")
        gm_tp: int = self.total_plant
        gm_tg: int = self.total_gr
        print(f"Plants added: {gm_tp}, Total growth: {gm_tg}")
        r: int = 0
        f: int = 0
        p: int = 0
        for plant in self.garden:
            if plant.kind == "regular":
                r += 1
            elif plant.kind == "flowering":
                f += 1
            else:
                p += 1
        print(f"Plant types: {r} regular, {f} flowering, {p} prize flowers")
        print("\n")
        value: bool = GardenManager.validate_height(self.garden)
        print(f"Height validation test: {value}")
        sc_a: int = GardenManager.GardenStats.calcul_stat(self.garden)
        print(f"Garden scores - {self.name}: {sc_a}, Bob: 92")
        GardenManager.create_garden_network()


if __name__ == "__main__":

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    alice = GardenManager("Alice's Garden")
    bob = GardenManager("Bob garden's")
    print("=== Garden Management System Demo ===\n")
    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)
    print("\n")
    alice.growth()
    alice.affiche_stat_garden()
