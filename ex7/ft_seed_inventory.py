def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if(unit == "packets"):
        print(seed_type.capitalize(),"seeds:",quantity,unit,"availble")
    elif(unit == "grams"):
        print(seed_type.capitalize(),"seeds:",quantity,unit,"total")
    elif(unit == "area"):
         print(seed_type.capitalize(),"seeds:",quantity,unit,"meters")
    else:
        print("Unknown unit type")


#ft_seed_inventory("tomato", 15, "packets")
#ft_seed_inventory("carrot", 8, "grams")
#ft_seed_inventory("lettuce", 12, "area")
#ft_seed_inventory("lettuce", 12, "are")