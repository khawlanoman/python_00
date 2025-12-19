def ft_count_harvest_recursive(days:int):
    if days == 0:
        return 

    ft_count_harvest_recursive(days - 1)
    print("day",days)

days = int(input("Days until harvest:"))
ft_count_harvest_recursive(5)
print("Harvest time!")