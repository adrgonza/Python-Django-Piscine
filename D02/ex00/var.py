def my_var():
    nb1 = 42
    str1 = "42"
    str2 = "quarante-deux"
    nb2 = 42.0
    blean = True
    lst = [42]
    dct = {
        42 : 42
    }
    tupl = (42,)
    my_set = set()
    variables = [nb1, str1, str2, nb2, blean, lst, dct, tupl, my_set]
    for var in variables:
        print(f'{var} has a type {type(var)}')

if __name__ == '__main__':
    my_var()