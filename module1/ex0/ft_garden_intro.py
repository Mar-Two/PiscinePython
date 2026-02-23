#!/usr/bin/env python3
def ft_garden_intro() -> None:
    """
    Affiche les détails d'une plante spécifique dans le jardin.
    Les données sont stockées dans des variables locales.
    """
    name: str = "Rose"
    height: int = 18
    age: int = 24

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
