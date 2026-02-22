def main() -> None:
    """Introduction au Set."""
    alice: set = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob: set = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie: set = {'level_10', 'treasure_hunter', 'boss_slayer',
                    'speed_demon', 'perfectionist'}
    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements:: {bob}")
    print(f"Player charlie achievements: {charlie}\n")
    print("=== Achievement Analytics ===")
    res_all: set = alice.union(bob, charlie)
    print(f"All unique achievements: {res_all}")
    taille: int = len(res_all)
    print(f"Total unique achievements: {taille}\n")
    res_inter: set = alice.intersection(bob, charlie)
    print(f"Common to all players: {res_inter}")
    union_alice_bob: set = alice.union(bob)
    only_charlie: set = charlie.difference(union_alice_bob)
    union_alice_charlie: set = alice.union(charlie)
    only_bob: set = bob.difference(union_alice_charlie)
    union_bob_charlie: set = bob.union(charlie)
    only_alice: set = alice.difference(union_bob_charlie)
    rare_achievements: set = only_alice.union(only_bob, only_charlie)
    print(f"Rare achievements (1 player): {rare_achievements}\n")
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
