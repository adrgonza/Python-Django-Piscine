from path import Path

def main():
    try:
        Path.makedirs('myfolder')
    except FileExistsError as e:
        print(e)
    
    Path.touch('myfolder/myfile')
    f = Path('myfolder/myfile')
    f.write_lines(['my', 'words'])
    print(f.read_text())

if __name__ == "__main__":
    main()
    