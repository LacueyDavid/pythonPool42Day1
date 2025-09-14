def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    if obj_type == int and object == 0:
        print("Zero : 0", obj_type)
        return 0
    elif object is None:
        print("Nothing: None", obj_type)
        return 0
    elif obj_type == float and object != object:
        print("Cheese: nan", obj_type)
        return 0
    elif object == "":
        print("Empty", obj_type)
        return 0
    elif object is False:
        print("Fake: False", obj_type)
        return 0
    else:
        print("Type not found")
        return 1
