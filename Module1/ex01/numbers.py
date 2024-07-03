if __name__ == '__main__':
    f = open("numbers.txt", "r")
    numbers = f.read().split(",")
    for nb in numbers:
        print(nb + '\n')