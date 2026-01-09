def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if(unit == "packets"):
        print(seed_type.capitalize(),"seeds:",quantity,unit,"availble")
    elif(unit == "grams"):
        print(seed_type.capitalize(),"seeds:",quantity,unit,"total")
    elif(unit == "area"):
         print(seed_type.capitalize(),"covers","seeds:",quantity,unit,"meters")
    else:
         print(seed_type.capitalize(),"seeds:",quantity,"Unknown unit type")