def display_list() -> None:
    """List comprehension."""
    my_list: list = [['alice', 2300, True], ['bob', 1800, True],
                     ['charlie', 2150, True], ['diana', 2050, False]]
    high_score: list = [x[0] for x in my_list if x[1] > 2000]
    score_doubl: list = [x[1] * 2 for x in my_list]
    active_player: list = [x[0] for x in my_list if x[2]]
    print(f"High scorers (>2000): {high_score}")
    print(f"Scores doubled: {score_doubl}")
    print(f"Active players: {active_player}\n")


def display_dict() -> None:
    """Dict comprehension."""
    player: dict = {
        "alice": {"score": 2300, "achievements": 5},
        "bob": {"score": 1800, "achievements": 3},
        "charlie": {"score": 2150, "achievements": 7}
    }
    cat_score: dict = {
        'high': len([n for n, score in player.items()
                     if score['score'] > 2200]),
        'medium': len([n for n, score in player.items()
                       if score['score'] > 2100]),
        'low': len([n for n, score in player.items()
                    if score['score'] >= 1800])
    }
    new_player: dict = {name: stats["score"] for name, stats in player.items()}
    achiev: dict = {name: achiv['achievements'] for name,
                    achiv in player.items()}
    print(f"Player scores: {new_player}")
    print(f"Score categories: {cat_score}")
    print(f"Achievement counts: {achiev}\n")


def display_set() -> None:
    """Set comprehension."""
    players: list = [
        ["alice", 2300, True, ["first_kill", "level_10"], "north"],
        ["bob", 1800, True, ["first_kill", "treasure_hunter"], "north"],
        ["charlie", 2150, True, ["level_10", "boss_slayer"], "east"],
        ["diana", 2050, False, ["collector", "speed_demon"], "central"],
        ["diana", 2050, False, ["collector", "speed_demon"], "west"]
    ]
    name_unique: set = {p[0] for p in players}
    achiev_unique: set = {ach for p in players for ach in p[3]}
    unique_pos: set = {p[4] for p in players}
    print(f"Unique players: {name_unique}")
    print(f"Unique achievements: {achiev_unique}")
    print(f"Active regions: {unique_pos}\n")


def analyse_all() -> None:
    """Analyse des différents Player."""
    players: list = [
        ["alice", 2300, True, ["first_kill", "level_10"], "north"],
        ["bob", 1800, True, ["first_kill", "treasure_hunter"], "north"],
        ["charlie", 2150, True, ["level_10", "boss_slayer"], "east"],
        ["diana", 2050, False, ["collector", "speed_demon"], "central"],
    ]
    print(f"Total players: {len(players)}")
    x = len([ach for p in players for ach in p[3]])
    print(f"Total unique achievements: {x}")
    total_score: int = sum(s[1] for s in players)
    res: float = total_score / len(players)
    t_p = max(players, key=lambda x: x[1])
    print(f"Average score: {res:.1f}")
    print(
        f"Top performer: {t_p[0]} ({t_p[1]} points,"
        f"{len(t_p[3])} achievements)")


if __name__ == "__main__":
    print("=== List Comprehension Examples ===")
    display_list()
    print("=== Dict Comprehension Examples ===")
    display_dict()
    print("=== Set Comprehension Examples ===")
    display_set()
    print("=== Combined Analysis ===")
    analyse_all()
