import sys


if __name__ == "__main__":
    try:
        f = open("ancient_fragment.txt", 'r')
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        print("Accessing Storage Vault: ancient_fragment.txt")
        print("Connection established...")
        print("RECOVERED DATA:")
        print(f.read())
        f.close()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.",
              file=sys.stderr)
