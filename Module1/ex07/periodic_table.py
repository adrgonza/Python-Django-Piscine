import sys

def write_body(file, elements_dict):
    content = '''
        <body>
            <header>
                <h1>Periodic Table</h1>
            </header>
            <main>
                <table border = 1>
    '''
    for i in range():
    file.write(content)

def write_head(file):
    content = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Periodic Table</title>
            <style>
                
            </style>
        </head>
    '''
    file.write(content)

def fill_html(elements_dict):
    file = open("./periodic_table.html", w)

    write_head(file)
    write_body(file, elements_dict)

    file.close()

def transform_str_to_dict(x, elements_dict):
    parts = x.split(", ")
    name = parts[0].split(" = ")[0]
    position = parts[0].split(" = ")[1].split(":")[1]
    number = parts[1].split(":")[1]
    small = parts[2].split(": ")[1]
    molar = parts[3].split(":")[1]
    electron = parts[4].split(":")[1]
    key = int(number)
    elements_dict[key] = {
        "name": name,
        "position": position,
        "small": small,
        "molar": molar,
        "electron": electron
    } 

def fill_dict(elements_dict):
    f = open("periodic_table.txt", "r")
    elements = f.read().split("\n")
    for x in elements:
        if x:
            transform_str_to_dict(x, elements_dict)
    elements_dict = dict(sorted(elements_dict.items()))
    print(elements_dict)

if __name__ == '__main__':
    elements_dict = {}

    fill_dict(elements_dict)
    fill_html(elements_dict)