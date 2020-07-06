from pdf2image import convert_from_bytes
import numpy as np
import cv2
import os


def convert(file, dpi=300, image_format='jpeg', color_mode='rgb'):
    """
    Convert pdf file to selected format

    Args:
        file (str or bytes):
            File or path to PDF file that need to be converted
        dpi (int):
            DPI of converter
        image_format (str):
            format of output file. Possible formats: ['jpeg', 'png']
        color_mode (str):
            Color mode of output images
            Possible modes: ['rgb', 'rgba', 'grayscale', 'binary']
    Returns:
        converted (list): list of converted pages
    """
    transparent = color_mode == 'rgba'
    grayscale = color_mode == 'grayscale'

    if type(file) == str:
        with open(file, 'rb') as f:
            file = f.read()
    converted = convert_from_bytes(file, dpi, fmt=image_format,
                                   transparent=transparent, grayscale=grayscale)
    converted = [np.array(im) for im in converted]
    if color_mode == 'binary':
        converted = [cv2.threshold(
            cv2.cvtColor(im, cv2.COLOR_RGB2GRAY), 128,
            255, cv2.THRESH_BINARY)[1] for im in converted]
    # elif color_mode == 'rgb':
    #     converted = [cv2.cvtColor(im, cv2.COLOR_BGR2RGB) for im in converted]
    # elif color_mode == 'rgba':
    #     converted = [cv2.cvtColor(im, cv2.COLOR_BGRA2RGBA) for im in converted]
    # elif color_mode == 'grayscale':
    #     converted = [cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) for im in converted]
    return converted


def get_file_name(file_path):
    return os.path.basename(file_path).split('.')[0]