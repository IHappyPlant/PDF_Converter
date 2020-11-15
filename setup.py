# coding=utf-8
"""
This module contains code for deploying PDF converter application
"""
from setuptools import setup

required_packages = [
    'pyqt5',
    'pdf2image',
    'numpy',
    'opencv-Python'
]

setup(
    name='pdf_converter',
    version='1.0',
    url='https://github.com/IHappyPlant/Pdf_Converter',
    author='IHappyPlant',
    author_email='karuk1998@yandex.ru',
    license='GPLv3',
    description='GUI app to converting files from PDF to image formats',
    packages=["converter"],
    install_requires=required_packages,
    include_package_data=True,
    python_requires='>=3.6',
    keywords="pdf jpg png converter image format gui application app",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Education'
    ]
)
