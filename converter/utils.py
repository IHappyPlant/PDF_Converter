"""This module contains utility functions for pdf converter."""
import os
from os.path import basename, splitext

from numpy import array
from pdf2image import convert_from_path


def convert(file, dpi=300, image_format='jpg', color_mode='rgb'):
    """
    Convert pdf file to selected format.

    :param str file: Path to PDF file that need to be converted
    :param int dpi: DPI of converter
    :param str image_format: format of output file.
        Possible formats: ['jpg', 'png']
    :param str color_mode: Color mode of output images.
        Possible modes: ['rgb', 'rgba', 'grayscale']
    :return: list of converted pages
    :rtype: list[numpy.ndarray]
    """
    cpu_count = os.cpu_count() or 1

    transparent = color_mode == 'rgba'
    grayscale = color_mode == 'grayscale'

    # Convert document to list of Pillow images
    converted = convert_from_path(file, dpi, fmt=image_format,
                                  transparent=transparent, grayscale=grayscale,
                                  thread_count=cpu_count)

    return [array(im) for im in converted]


def get_file_name(file_path):
    """
    :param str file_path: Path to file
    :return: Name of file without extension
    :rtype: str
    """
    return splitext(basename(file_path))[0]
