#!/bin/bash
# Create binary file using pyinstaller
venv_name="/tmp/temp_venv_$RANDOM"
executable_name=pdf_converter
pip3 install virtualenv
python3 -m venv $venv_name
source "$venv_name/bin/activate"
pip install --no-cache-dir pyinstaller pyqt5 pdf2image numpy pillow
pyinstaller converter/__main__.py --onefile --clean -n"$executable_name"
deactivate

rm "$executable_name.spec"
rm -rf build "$venv_name"
