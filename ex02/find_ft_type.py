def all_thing_is_obj(object: any) -> int:
    if object.__class__ is list:
        print("List :", object.__class__)
    elif object.__class__ is tuple:
        print("Tuple :", object.__class__)
    elif object.__class__ is set:
        print("Set :", object.__class__)
    elif object.__class__ is dict:
        print("Dict :", object.__class__)
    elif object.__class__ is str:
        print(f"{object} is in the kitchen :", object.__class__)
    else:
        print("Type not found")
    return 42
