# Pdf to image
This application is designed to simplify converting data from PDF to PNG 
or JPG format.  

With this application, you can easily convert PDF documents, even if they have 
multiple pages, to images.  

![PDF converter screenshot](imgs/pdf_converter_screenshot.png)

## Installation
Application can be installed directly to Python then used as Python module, or
you can build binary executable file from source.

### Python
Clone repository:
```shell
git clone https://github.com/IHappyPlant/PDF_Converter.git
```
Install converter to Python:
```shell
python setup.py install
```
Run the application:
```shell
python -m converter
```

### Building binary
You can build binary executable file for your platform using installation 
scripts from the repository root. There are installation scripts for *nix
systems.

Clone repository:
```shell
git clone https://github.com/IHappyPlant/PDF_Converter.git
```
And run installation script for your OS:
```shell
./install.sh
```
for Linux or:
```shell
.\install.bat
```
for Windows.  
This will generate "dist" directory in the repository root with single 
executable file inside.

**Warning**: For now, only building binary for Linux is supported. On Windows, for unknown
reason PyInstaller can't build executable when running from venv. It works
correctly only if packages installed in global environment.

### Windows specific
For Windows, you must also download 
[poppler](https://blog.alivate.com.au/poppler-windows/) for Windows, and add 
its ```bin/``` folder to PATH.  
Then, you can download and run the latest application release for Windows, or 
install application [directly to Python](#python).
 
### Other
You can also just download and run latest application release for Linux or 
Windows from releases.  

For some Linux distros you may need also install ```poppler-utils``` package 
with your package manager.
