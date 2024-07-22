pip3 --version

rm -rf local_lib

mkdir local_lib

git clone https://github.com/jaraco/path local_lib > "path_install.log"

pip3 install ./local_lib/. >> "path_install.log" 2>&1

if [ $? -eq 0 ]; then
    echo "Installation successful. Running the Python program..."
    python3 my_program.py
else
    echo "Installation failed. Check the log file for details."
fi