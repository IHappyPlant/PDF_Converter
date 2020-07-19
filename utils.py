import os

import cv2
import numpy as np
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
        converted (list): list of converted pages
    """
    transparent = color_mode == 'rgba'
    grayscale = color_mode == 'grayscale'

    with open(file, 'rb') as f:
        file = f.read()
    converted = convert_from_bytes(file, dpi, fmt=image_format,
                                   transparent=transparent, grayscale=grayscale)
    if color_mode == 'rgb':
        converted = [cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
                     for im in converted]
    elif color_mode == 'rgba':
        if image_format != 'jpg':
            converted = [cv2.cvtColor(np.array(im), cv2.COLOR_RGBA2BGRA)
                         for im in converted]
        else:
            converted = [cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
                         for im in converted]
    elif color_mode == 'binary':
        converted = [cv2.cvtColor(cv2.threshold(
            cv2.cvtColor(np.array(im), cv2.COLOR_RGB2GRAY), 128,
            255, cv2.THRESH_BINARY)[1], cv2.COLOR_GRAY2BGR) for im in converted]
    else:
        # Grayscale
        converted = [
            cv2.cvtColor(cv2.cvtColor(np.array(im), cv2.COLOR_RGB2GRAY),
                         cv2.COLOR_GRAY2BGR)
            for im in converted]
    return converted


def get_file_name(file_path):
    return os.path.basename(file_path).split('.')[0]
