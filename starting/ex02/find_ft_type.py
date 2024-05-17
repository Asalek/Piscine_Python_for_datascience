def all_thing_is_obj(object: any) -> int:
    types = {
        str  : "String",
        tuple: "Tuple",
        dict : "Dict",
        set  : "Set",
        list : "List"
    }
    o_type = object.__class__
    object_type = types.get(o_type, "Type not found")#Return the value for key if key is in the dictionary, else type Not found.
    if o_type == str:
        print(f"{object} is in the kitchen : {o_type}")
    elif object_type != "Type not found":
        print(f"{object_type} : {o_type}")
    else:
        print(f"{object_type}")
    return 42

# def main():
# 	ft_list = ["Hello", "tata!"]
# 	ft_tuple = ("Hello", "toto!")
# 	ft_set = {"Hello", "tutu!"}
# 	ft_dict = {"Hello" : "titi!"}
# 	all_thing_is_obj(ft_list)
# 	all_thing_is_obj(ft_tuple)
# 	all_thing_is_obj(ft_set)
# 	all_thing_is_obj(ft_dict)
# 	all_thing_is_obj("Brian")
# 	all_thing_is_obj("Toto")
# 	print(all_thing_is_obj(10))

# if __name__ == "__main__":
# 	main()