ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Assign to Array :
ft_list[1] = 'World!'
# Assign to tuple
tuple_lst = list(ft_tuple)
tuple_lst[1] = 'Morocco!'
ft_tuple = tuple(tuple_lst)

# Assign to set
ft_set.remove("tutu!")
ft_set.add("khouribga!")
# Assign to dict
ft_dict["Hello"] = '1337!'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
