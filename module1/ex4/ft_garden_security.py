"""Module de gestion sécurisée des données."""


class SecurePlant:
    """Représente une plante avec des attributs protégés."""
    def __init__(self, name: str) -> None:
        """Initialise une nouvelle instance de SecurePlant."""
        self.name = name
        self._height = 0
        self._age = 0

    def get_height(self) -> int:
        """Retourne la taille actuel de la plante en cm."""
        return self._height

    def get_age(self) -> int:
        """Retourne l'âge actuel de la plante en jours."""
        return self._age

    def set_height(self, height: int) -> None:
        """Fonction de validation du paramètre height."""
        if height >= 0:
            self._height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        """Fonction de validation du paramètre age."""
        if age >= 0:
            self._age = age
            print(f"Age updated: {age} days [OK]\n")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")


def ft_secure_plant() -> None:
    """Fonction qui declare l'objet plante et change la valeur height et age"""
    print("=== Garden Security System ===")
    plante = SecurePlant("Rose")
    print(f"Plant created: {plante.name}")
    plante.set_height(25)
    plante.set_age(30)
    plante.set_height(-5)
    height: int = plante.get_height()
    age: int = plante.get_age()
    print(f"\nCurrent plant: {plante.name} ({height}cm, {age} days)")


if __name__ == "__main__":
    ft_secure_plant()
