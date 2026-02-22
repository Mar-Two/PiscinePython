import sys


def main() -> None:
    """Reçois des arguments les tries et les analyses."""
    if len(sys.argv) < 2:
        print("Veuilliez insérer de l'inventaires")
        return

    inventory: dict = {}
    for arg in sys.argv[1:]:
        if ":" in arg:
            name, qty = arg.split(":")
            inventory[name] = {"quantity": int(qty)}
    total_items: int = sum(item['quantity'] for item in inventory.values())

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory.keys())}")

    print("\n=== Current Inventory ===")

    sorted_items: list = sorted(inventory.items(),
                                key=lambda x: x[1]['quantity'], reverse=True)
    for name, data in sorted_items:
        qty: int = data['quantity']
        res: float = (qty / total_items) * 100 if total_items > 0 else 0.0
        unit_str: str = "unit" if qty == 1 else "units"
        print(f"{name}: {qty} {unit_str} ({res:.1f}%)")

    print("\n=== Inventory Statistics ===")
    maxv: tuple = sorted_items[0]
    minv: tuple = sorted_items[-1]
    print(f"Most abundant: {maxv[0]} ({maxv[1]['quantity']} units)")
    print(f"Least abundant: {minv[0]} ({minv[1]['quantity']} unit)")

    print("\n=== Item Categories ===")
    categories: dict = {"Moderate": {}, "Scarce": {}}
    for name, data in inventory.items():
        q: int = data['quantity']
        if q >= 5:
            categories["Moderate"][name] = q
        else:
            categories["Scarce"][name] = q
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")

    print("\n=== Management Suggestions ===")
    restock: list = [name for name, data in inventory.items()
                     if data['quantity'] <= 1]
    print(f"Restock needed: {restock}")
    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    val_list: list = [v['quantity'] for v in inventory.values()]
    print(f"Dictionary values: {val_list}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    main()
