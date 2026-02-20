
if __name__ == "__main__":
    my_list: list = ["lost_archive.txt", "classified_vault.txt",
                     "standard_archive.txt"]
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        print("CRISIS ALERT: Attempting access to'lost_archive.txt'...")
        with open(my_list[0], 'r') as f1:
            print(f1.read())
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    try:
        print("CRISIS ALERT: Attempting access to'classified_vault.txt'...")
        with open(my_list[1], 'r') as f2:
            f2.read()
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    try:
        print("ROUTINE ACCESS: Attempting access to'standard_archive.txt'...")
        with open(my_list[2], 'r') as f3:
            data: str = f3.read()
            print(f"SUCCESS: Archive recovered - ``{data}''")
            print("STATUS: Normal operations resumed\n")
    except Exception as e:
        print("Global Error :", e)
    print("All crisis scenarios handled successfully. Archives secure.")
