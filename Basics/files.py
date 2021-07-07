def run():
    read()
    write()


def read():
    nums = []
    # encoding="utf-8" all chars are accepted
    with open("/Volumes/Mec/AFGZB/Documents/Portofolio/Python/Basics/files/nums.txt", "r", encoding="utf-8") as f:
        for line in f:
            nums.append(int(line))
    print(nums)

def write():
    chars = ["a", "b", "c", "d", "e", "ñ", "á"]
    with open("/Volumes/Mec/AFGZB/Documents/Portofolio/Python/Basics/files/names.txt", "w", encoding="utf-8") as f:
        for c in chars:
            f.write(c)
            f.write("\n")

if __name__ == '__main__':
    run()