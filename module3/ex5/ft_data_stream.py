from typing import Generator
import time
import math


def data_stream(n: int) -> Generator[dict, None, None]:
    """Crée un dict representant un event en direct."""
    nom: list = ['alice', 'bob', 'charlie', 'diana', 'eve', 'frank']
    level: list = [5, 12, 8]
    action: list = ['killed monster', 'found treasure', 'leveled up']
    for i in range(n):
        events: dict = {
            'id': i + 1,
            'player': nom[i % len(nom)],
            'level': level[i % len(level)],
            'action': action[i % len(action)]
        }
        if events['action'] == 'leveled up':
            events['level'] += 1
        yield events


def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    k: int = int(math.sqrt(n))
    for i in range(3, k + 1, 2):
        if n % i == 0:
            return False
    return True


def number_prime(n: int) -> Generator[int, None, None]:
    k: int = 0
    count = 0
    while count < n:
        if is_prime(k):
            yield k
            count += 1
        k += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    n: int = 1000
    print(f"Processing {n} game events...")
    level_up: int = 0
    count: int = 0
    event_level: int = 0
    tresor: int = 0
    s = time.process_time()
    for data in data_stream(n):
        if data['id'] < 4:
            print(
                f"Event {data['id']}: Player {data['player']}"
                f" (level {data['level']}) {data['action']}"
            )
        if data['id'] == 5:
            print("...\n")
        count += 1
        if data['action'] == 'found treasure':
            tresor += 1
        if data['action'] == 'leveled up':
            event_level += 1
        if data['level'] >= 10:
            level_up += 1
    e = time.process_time()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {n}")
    print(f"High-level players (10+): {level_up}")
    print(f"Treasure events: {tresor}")
    print(f"Level-up events: {event_level}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {e - s:.4f} seconds\n")
    print("=== Generator Demonstration ===")
    print(f"Fibonacci sequence (first 10): {list(fibonacci(10))}")
    print(f"Prime numbers (first 5): {list(number_prime(5))}")
