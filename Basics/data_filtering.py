from var_data import DATA


def run():
    # List and Dict comprehension
    all_python_devs = [
        worker["name"] for worker in DATA if worker["language"] == "python"
    ]


if __name__ == '__main__':
    run()
