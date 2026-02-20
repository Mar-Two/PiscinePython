

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")
    print("Storage unit created successfully...\n")
    fw = open("new_discovery.txt", 'w')
    my_list: list = ["New quantum algorithm discovered",
                     "Efficiency increased by 347%",
                     "Archived by Data Archivist trainee"]
    i: int = 1
    print("Inscribing preservation data...")
    for my_l in my_list:
        entry: str = f"[ENTRY 00{i}] {my_l}"
        fw.write(entry + '\n')
        print(entry)
        i += 1
    fw.close()
    print("\nData inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")
