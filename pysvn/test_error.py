def add_numbers(a, b):
    return a + b

def wrong_param_type(n: int):
    print(n)

if __name__ == "__main__":
    result = add_numbers("1", 2)

    wrong_param_type("123")

    my_dict = {"apple": 3, "banana": 5, "cherry": 2}
    print(my_dict["mango"])

    my_list = [5, 6, 7]
    print(my_list[3])