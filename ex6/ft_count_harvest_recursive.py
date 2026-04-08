def ft_count_harvest_recursive(harvest=None, day=1):
    harvest = harvest or int(input("Days until harvest: "))
    if day > harvest:
        return print("Harvest time!")
    print("Day", day)
    ft_count_harvest_recursive(harvest, day + 1)
