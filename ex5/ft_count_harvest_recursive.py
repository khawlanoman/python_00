def ft_count_harvest_recursive(day=None, c=1):
    if day is None:
        day = int(input("Days until harvest:"))
    if c > day:
        print("Harvest time!")
        return
    print("Day", c)
    return ft_count_harvest_recursive(day, c + 1)