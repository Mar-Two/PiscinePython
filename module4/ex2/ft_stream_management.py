import sys

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    id: str = input("Input Stream active. Enter archivist ID: ")
    archv: str = input("Input Stream active. Enter status report: ")
    print(f"[STANDARD] Archive status from {id}: {archv}",
          file=sys.stdout)
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print("Three-channel communication test successful.", file=sys.stdout)
