def all_thing_is_obj(object: any) -> int:
    
    if isinstance(object, list):
        print("List : <class 'list'>")
    elif isinstance(object, tuple):
        print("Tuple : <class 'tuple'>")
    elif isinstance(object, set):
        print("Set : <class 'set'>")
    elif isinstance(object, dict):
        print("Dict : <class 'dict'>")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : <class 'str'>")
    else:
        print("Type not found$")
    return  42




ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))
