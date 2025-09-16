def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing :", object.__class__)
    elif object.__class__ is float and object != object:
        print("Cheese :", object.__class__)
    elif object.__class__ is int and object == 0:
        print("Zero :", object.__class__)
    elif object == '':
        print("Empty :", object.__class__)
    elif object is False:
        print("Fake :", object.__class__)
    else:
        print("Type not Found")
        return 1
    return 0
