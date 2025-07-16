def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing : <class 'NoneType'>")
    elif isinstance(object , float) and object != object:
        print("Cheese : nan  <class 'float'>")
    elif isinstance(object, bool) and object is False:
        print("Fake : False <class 'bool'>")
    elif isinstance(object, str) and object == "":
        print("Empty : <class 'str'>")
    elif isinstance(object, int) and object == 0:
        print("Zero :0  <class 'int'>")
    else :
        print("Type not Found")
        return 1
    return 0



Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
