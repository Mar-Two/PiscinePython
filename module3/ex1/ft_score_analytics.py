import sys


def main() -> None:
    """Recois des arguments les parses et Analyse les scores."""
    n: int = len(sys.argv)
    print("=== Player Score Analytics ===")
    if n <= 1:
        c: str = "python3 ft_score_analytics.py <score1> <score2> ..."
        print(f"No scores provided. Usage: {c}")
    else:
        try:
            j: int = 1
            k: int = 0
            res_list: list = [0] * (n - 1)
            while j < n:
                res_list[k] += int(sys.argv[j])
                j += 1
                k += 1
            print(f"Scores processed: {res_list}")
            print(f"Total players: {n - 1}")
            s: int = sum(res_list)
            print(f"Total score: {s}")
            m: float = s / (n - 1)
            print(f"Average score: {m}")
            h_s: int = max(res_list)
            print(f"High score: {h_s}")
            l_s: int = min(res_list)
            print(f"Low score: {l_s}")
            s_r = h_s - l_s
            print(f"Score range: {s_r}")
        except ValueError:
            print("Error: All scores must be integers.")


if __name__ == "__main__":
    main()
