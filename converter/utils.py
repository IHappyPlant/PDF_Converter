# coding=utf-8
"""
This module contains utility functions for pdf converter
"""
from os.path import basename, splitext

import cv2
from numpy import array
from pdf2image import convert_from_bytes


def convert(file, dpi=300, image_format='jpg', color_mode='rgb'):
    """
    Convert pdf file to selected format

    Args:
        file (str):
            Path to PDF file that need to be converted
        dpi (int):
            DPI of converter
        image_format (str):
            format of output file. Possible formats: ['jpg', 'png']
        color_mode (str):
            Color mode of output images
            Possible modes: ['rgb', 'rgba', 'grayscale', 'binary']
    Returns:
        converted (list of numpy.ndarray): list of converted pages
    """
    transparent = color_mode == 'rgba'
    grayscale = color_mode == 'grayscale'

    with open(file, 'rb') as f:
        file = f.read()
    # Convert document to Pillow images
    converted = convert_from_bytes(file, dpi, fmt=image_format,
                                   transparent=transparent,
                                   grayscale=grayscale)
    # Convert colors from RGB(A) to BGR(A)
    if color_mode == 'rgb':
        converted = [cv2.cvtColor(array(im), cv2.COLOR_RGB2BGR)
                     for im in converted]
    elif color_mode == 'rgba':
        if image_format != 'jpg':
            converted = [cv2.cvtColor(array(im), cv2.COLOR_RGBA2BGRA)
                         for im in converted]
        else:
            converted = [cv2.cvtColor(array(im), cv2.COLOR_RGB2BGR)
                         for im in converted]
    elif color_mode == 'binary':
        # Apply binary threshold to image
        converted = [cv2.threshold(
            cv2.cvtColor(array(im), cv2.COLOR_RGB2GRAY), 128, 255,
            cv2.THRESH_BINARY)[1] for im in converted]
    else:
        # Convert RGB to grayscale
        converted = [cv2.cvtColor(array(im), cv2.COLOR_RGB2GRAY)
                     for im in converted]
    return converted


def get_file_name(file_path):
    """
    Get name of the file

    Args:
        file_path (str): Path to file
    Returns:
        (str): Name of file without extension
    """
    return splitext(basename(file_path))[0]
