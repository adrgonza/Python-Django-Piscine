import sys

def write_body(file, elements_dict):
    content = '''
        <body>
            <header>
                <h1>Periodic Table</h1>
            </header>
            <main>
                <table class="periodic-table">
    '''
    max_index = max(elements_dict.keys())
    index = 1
    for i in range(7):
        content += '<tr>\n'
        for j in range(18):
            while index <= max_index:
                try :
                    element = elements_dict[index]
                    if int(element["position"]) == j:
                        content += f'''
                                    <td style="border: 1px solid black; padding:0px">
                                        <h4>{elements_dict[index]["name"]}</h4>
                                            <ul>
                                                <li>{index} {elements_dict[index]["small"]}</li>
                                                <li>{elements_dict[index]["molar"]}</li>
                                                <li>{elements_dict[index]["electron"]} electrons</li>
                                            </ul>
                                    </td>
                        '''
                        index += 1
                    else:
                        content += '<td style="border: 1px solid black; padding:10px"></td>'
                    break
                except:
                    index += 1
        content += '</tr>\n'
    content += '''
                </table>
            </main>
        </body>
    </html>
    '''
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
                body {
                    text-align: center;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    border: 1px solid black;
                    text-align: center;
                }
                h4 {
                    font-size: 11px;
                    margin-top: 0;
                    text-align: center;
                }
                ul {
                    list-style-type: none;
                    padding: 0;
                    text-align: center;
                    margin-top: 0px;
                }
                li {
                    font-size: 12px;
                }
            </style>
        </head>
    '''
    file.write(content)

def fill_html(elements_dict):
    file = open("./periodic_table.html", "w")

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