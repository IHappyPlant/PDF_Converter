set venv_name=temp_venv_%RANDOM%
set executable_name=pdf_converter
pip3 install virtualenv
python3 -m venv %venv_name%

.\%venv_name%\Scripts\activate.bat & ^
pip install pyinstaller pyqt5 pdf2image numpy pillow & ^
pyinstaller converter\__main__.py --windowed --clean -n%executable_name% & ^
del %executable_name%.spec & ^
rmdir /S /Q build & ^
rmdir /S /Q %venv_name%
