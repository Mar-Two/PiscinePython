import sys

if __name__ == "__main__":
    try:
        print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
        print("Initiating secure vault access...")
        with (open("classified_data.txt", 'r') as f1,
              open("security_protocols.txt", 'r') as f2):
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            print(f1.read())
            print("\nSECURE PRESERVATION:")
            print(f2.read())
            print("Vault automatically sealed upon completion")
            print("All vault operations completed with maximum security.")
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
