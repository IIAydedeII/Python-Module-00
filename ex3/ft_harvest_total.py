def ft_harvest_total():
    harvest = 0
    day = 1
    while day < 4:
        harvest += int(input(f"Day {day} harvest: "))
        day += 1
    print("Total harvest:", harvest)
