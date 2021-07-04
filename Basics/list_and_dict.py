def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {
        "firstname": "Angel",
        "lastname": "Zambrano"
    }

    super_list = [
        {1: "a"},
        {2: "b"},
        {3: "c"}
    ]

    super_dict = {
        "natural": [1,2,3,4],
        "integer": [1,-2,3,-4]
    }

    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == '__main__':
    run()