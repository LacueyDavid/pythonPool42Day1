ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}
# your code here

# list modification
ft_list[1] = "World!"

# tuple is immutable so you have to transform to list and then to tuple
my_list = list(ft_tuple)
my_list[1] = "France!"
ft_tuple = tuple(my_list)

# set you have to remove
ft_set.remove("tutu!")
ft_set.add("Paris!")

# ft_dict
ft_dict["Hello"] = "42Paris!"

# print result,,
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# result have to be:
# ['Hello', 'World!']$
# ('Hello', 'France!')$
# {'Hello', 'Paris!'}$
# {'Hello': '42Paris!'}$
# $>
