#!/usr/bin/env python3

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'local_lib'))

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
    