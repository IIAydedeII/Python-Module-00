def ft_count_harvest_iterative():
    harvest = int(input("Days until harvest: "))
    for day in range(harvest):
        print("Day", day + 1)
    print("Harvest time!")
