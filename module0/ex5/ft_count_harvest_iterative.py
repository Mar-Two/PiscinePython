def ft_count_harvest_iterative() -> None:
    end = int(input("Days until harvest: "))
    x = range(1, end + 1)
    for n in x:
        print("Day", n)
    print("Harvest Time!")
