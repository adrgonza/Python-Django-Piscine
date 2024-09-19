# #!/bin/bash

GITURL="https://github.com/jaraco/path.git"

python3 -m venv venv
source venv/bin/activate

echo "Pip version:"
pip --version

pip install --target="local_lib" --log path_install.log --force-reinstall git+"$GITURL"

python my_program.py
