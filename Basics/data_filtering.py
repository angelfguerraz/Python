from var_data import DATA


def run():
    # List and Dict comprehension
    all_python_devs = [
        worker["name"] for worker in DATA if worker["language"] == "python"
    ]

    # Lambda functions
    adults = list(filter(lambda k: k["age"] >= 18, DATA))
    # adults_names = [i["name"] for i in adults]
    adults_names = list(map(lambda n: n["name"], adults))
    print(adults_names)

    old_ppl = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))


if __name__ == '__main__':
    run()
