if __name__ == '__main__':
    try:
        with open("numbers.txt", "r") as f:
            numbers = f.read().split(",")
            for nb in numbers:
                print(nb)
    except FileNotFoundError:
        print("Wrong file or file path")
