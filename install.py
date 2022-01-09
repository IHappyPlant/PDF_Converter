"""
This module contains code to build executable file from converter code.
"""
import os
import shutil

import PyInstaller.__main__

EXECUTABLE_NAME = "pdf_converter"
cmd_args = [
    "converter/__main__.py",
    "--onefile",
    "--clean",
    f"-n{EXECUTABLE_NAME}",
]
windows_opts = ["--windowed"]
if os.name == "nt":
    cmd_args += windows_opts

if __name__ == '__main__':
    PyInstaller.__main__.run(cmd_args)
    shutil.rmtree("build", ignore_errors=True)
    os.remove(f"{EXECUTABLE_NAME}.spec")
